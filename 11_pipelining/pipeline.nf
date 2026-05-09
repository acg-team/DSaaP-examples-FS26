#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

/*
 * This pipeline takes FASTA files, aligns them with PRANK and MAFFT,
 * then runs two tools to infer phylogenies:  RAxML-ng 2.0.3beta with automatic model selection and
 * tree search, and BEAST 2.6.3 for Bayesian phylogenetic analysis.
 */

// Define parameters with default values
params.input = "data/*.fasta"
params.outdir = "results"

process preprocess_fasta {
    publishDir "${params.outdir}/cleaned_fasta", mode: 'copy'

    input:
    path fasta

    output:
    path "${fasta.baseName}.clean.fasta"

    script:
    """
    sed "s/\\['//g; s/']//g" ${fasta} > ${fasta.baseName}.clean.fasta
    """
}

process align_prank {
    publishDir "${params.outdir}/prank", mode: 'copy'

    input:
    path fasta

    output:
    path "${fasta.baseName}.prank.fasta"

    script:
    // PRANK's output is .best.fas, so we rename it for clarity.
    """
    prank -d=${fasta} -o=${fasta.baseName}.prank -F
    mv ${fasta.baseName}.prank.best.fas ${fasta.baseName}.prank.fasta
    """
}

process align_mafft {
    publishDir "${params.outdir}/mafft", mode: 'copy'

    input:
    path fasta

    output:
    path "${fasta.baseName}.mafft.fasta"

    script:
    """
    mafft --auto ${fasta} > ${fasta.baseName}.mafft.fasta
    """
}

process run_raxml_ng {
    publishDir "${params.outdir}/raxml", mode: 'copy'

    input:
    path alignment

    output:
    path "${alignment.baseName}.raxml.*"

    script:
    def model_args = alignment.name.contains('DNA') ? "--model DNA" : "--model AA --moose-options substitution-models=DCMut,JTT,JTT-DCMut,LG,PMB,Q.pfam,Q.yeast,VT,WAG,PROTGTR"
    """
    raxml-ng-2 --msa ${alignment} ${model_args} --opt-topology adaptive --prefix ${alignment.baseName}
    """
}

process generate_beast_xml {
    publishDir "${params.outdir}/beast_xml", mode: 'copy'

    input:
    path alignment

    output:
    path "*.xml"

    script:
    """
    python ${workflow.projectDir}/scripts/beast_configuration.py --alignment ${alignment} --output ${alignment.baseName}.xml
    """
}

process run_beast {
    publishDir "${params.outdir}/beast", mode: 'copy'
    cpus 4

    input:
    path xml

    output:
    path "*.log"
    path "*.trees"
    path "*.xml.state"

    script:
    """
    beast -threads ${task.cpus} -overwrite ${xml}
    """
}

workflow {
    println(
        """
    PKS Analysis Pipeline
    Input files: ${params.input}
    Output dir : ${params.outdir}
    """
    )

    // Create a channel for input files
    fasta_files_ch = channel.fromPath(params.input)

    // Preprocess FASTA files
    clean_fasta_ch = preprocess_fasta(fasta_files_ch)

    // Align sequences using both PRANK and MAFFT
    prank_alignments = align_prank(clean_fasta_ch)
    mafft_alignments = align_mafft(clean_fasta_ch)

    // Combine the results from both alignment tools into a single channel
    all_alignments = prank_alignments.mix(mafft_alignments)

    // Run RAxML-ng on each alignment
    run_raxml_ng(all_alignments)

    // Run BEAST on each alignment
    beast_xml_ch = generate_beast_xml(all_alignments)
    run_beast(beast_xml_ch)
}
