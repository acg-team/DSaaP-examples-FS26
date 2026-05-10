# Pipelining Example (DSaaP FS26)

This project demonstrates a simple Nextflow pipeline for phylogenetic analysis of FASTA inputs.

The main workflow is [pipeline.nf](pipeline.nf). It:

- cleans FASTA formatting artifacts;
- aligns each cleaned FASTA with PRANK and MAFFT in parallel;
- runs RAxML-NG on each alignment;
- generates BEAST XML files;
- runs BEAST on each generated XML.

## Requirements

- Nextflow 25+;
- micromamba or mamba;
- the Conda environment described in [environment.yml](./environment.yml);
- input FASTA files in [data](./data).

## Project Setup With `mamba`

The local `standard` profile in [nextflow.config](./nextflow.config) expects a Conda environment at:

```bash
/Users/pece/.local/share/mamba/envs/polyketide_analysis
```

Create that environment from the provided file:

```bash
# from this folder
mamba env create -p /Users/pece/.local/share/mamba/envs/polyketide_analysis -f environment.yml
```

If the environment already exists, update it with:

```bash
mamba env update -p /Users/pece/.local/share/mamba/envs/polyketide_analysis -f environment.yml --prune
```

## Input Data

The workflow reads FASTA files matching:

```bash
data/*.fasta
```

This is controlled by `params.input` in [pipeline.nf](./pipeline.nf). You can override it at runtime.

Example input layout:

```text
data/
├── example1.fasta
└── example2.fasta
```

## Running The Pipeline

Expected behaviour:

- each FASTA file is cleaned first;
- PRANK and MAFFT run in parallel on the cleaned FASTA;
- each alignment is passed to RAxML-NG and to BEAST XML generation;
- BEAST runs once per generated XML file;
- Nextflow writes execution reports under `results/pipeline_info/`.

### Run Locally

Run the workflow with the default settings:

```bash
nextflow run pipeline.nf
```

Run the workflow with a custom input glob and output directory:

```bash
nextflow run pipeline.nf \
    --input 'data/*.fasta' \
    --outdir results
```

Resume a previous run:

```bash
nextflow run pipeline.nf -resume
```

### Run on a SLURM Cluster

Run on a SLURM cluster with the `slurm` profile:

```bash
nextflow run pipeline.nf -profile slurm
```

Before using the SLURM profile, update the `slurm` block in [nextflow.config](./nextflow.config):

- set `process.conda` to a Conda or micromamba environment path visible on compute nodes;
- set `process.queue` to the partition name used on your cluster;
- replace `--account=<your_account>` with the correct SLURM account string for your project;
- add any other configuration necessary for that particular cluster environment.


### Run on the ZHAW SLURM Cluster

You will need to load the JDK and conda modules before running nextflow:

```bash
module purge
module load DefaultModules USS/2022 gcc/9.4.0-pe5.34 jdk/19
module load miniconda3/4.12.0 lsfm-init-miniconda/1.0.0
```

Run on the ZHAW SLURM cluster with the `slurm_zhaw` profile:

```bash
nextflow run pipeline.nf -profile slurm_zhaw
```

Before using the SLURM profile, update the `slurm_zhaw` block in [nextflow.config](./nextflow.config):

- set `process.conda` to a Conda environment path visible on compute nodes;
- asjust the time and memory constraints as needed.


## Pipeline Outputs

The workflow publishes results under `results/` by default:

```text
results/
├── cleaned_fasta/
├── prank/
├── mafft/
├── raxml/
├── beast_xml/
├── beast/
└── pipeline_info/
```

For one input file `example.fasta`, the expected main outputs are:

- `results/cleaned_fasta/example.clean.fasta`
- `results/prank/example.clean.prank.fasta`
- `results/mafft/example.clean.mafft.fasta`
- `results/raxml/example.clean.prank.raxml.*`
- `results/raxml/example.clean.mafft.raxml.*`
- `results/beast_xml/example.clean.prank.xml`
- `results/beast_xml/example.clean.mafft.xml`
- `results/beast/example.clean.prank.log`
- `results/beast/example.clean.prank.trees`
- `results/beast/example.clean.prank.xml.state`
- `results/beast/example.clean.mafft.log`
- `results/beast/example.clean.mafft.trees`
- `results/beast/example.clean.mafft.xml.state`

## What Each Process Does

The workflow contains the following processes in [pipeline.nf](./pipeline.nf):

- `preprocess_fasta`: removes `['` and `']` artifacts from each input FASTA.
- `align_prank`: runs `prank -d=<input> -o=<prefix> -F` and renames the `.best.fas` output.
- `align_mafft`: runs `mafft --auto <input>`.
- `run_raxml_ng`: runs `raxml-ng-2 --msa <alignment> ... --prefix <name>`.
- `generate_beast_xml`: runs [scripts/beast_configuration.py](./scripts/beast_configuration.py) to create a BEAST XML file.
- `run_beast`: runs `beast -threads <cpus> -overwrite <xml>`.

## DNA vs Protein Naming Convention

The workflow does not inspect sequence characters to decide whether an alignment is nucleotide or amino-acid data. Instead, it uses the file name.

- In [pipeline.nf](./pipeline.nf), `run_raxml_ng` checks `alignment.name.contains('DNA')`.
- If the file name contains `DNA`, the process runs RAxML-NG with `--model DNA`.
- Otherwise, it assumes the alignment is protein data and runs with `--model AA` plus the configured amino-acid model list.

The XML generator uses the same convention:

- if the alignment path contains `DNA`, [scripts/beast_configuration.py](./scripts/beast_configuration.py) selects [beast_template/dna_template.xml](./beast_template/dna_template.xml) and uses `totalcount="4"` for sequences;
- otherwise it selects [beast_template/protein_template.xml](./beast_template/protein_template.xml) and uses `totalcount="20"`.

Examples:

- `PKS_DNA.clean.mafft.fasta` will be treated as DNA.
- `PKS_AT.clean.mafft.fasta` will be treated as protein.

If your files do not follow that naming convention, both RAxML-NG model selection and BEAST template selection may be wrong.

## BEAST XML Generation

The `generate_beast_xml` step builds a BEAST XML configuration from each alignment by running [scripts/beast_configuration.py](./scripts/beast_configuration.py).

The script does the following:

- reads the input alignment with `dark.fasta.FastaReads`;
- chooses the default template XML based on whether the alignment path contains `DNA`;
- finds the `<data>` element in the template;
- replaces the template alignment id with the current alignment base name;
- updates references elsewhere in the XML that point to the old `<data>` id;
- appends one `<sequence>` element per FASTA record;
- sanitizes sequence ids for XML element ids by replacing non-alphanumeric characters with underscores;
- writes the final XML file to `results/beast_xml/`.

For each sequence, the generated XML contains a BEAST `<sequence>` element with:

- `id="seq_<sanitized_name>"`
- `taxon="<original FASTA header>"`
- `value="<aligned sequence>"`
- `totalcount="4"` for DNA or `totalcount="20"` for protein

The resulting XML is then passed unchanged to `beast -threads <cpus> -overwrite <xml>` in the next process.

## Notes

- The current [nextflow.config](./nextflow.config) defines a local `standard` profile and a `slurm` profile.

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP), Spring semester 2026 (FS26).

## License

Licensed under the MIT License. See [LICENSE](../LICENSE).
