# GC Content of Sequences

This is a basic Python script to calculate GC content from sequences in a fasta file.

## Setup

To run this little project you need Python3 installed on your machine.

```zsh
git clone git@github.com:acg-team/DSaaP-examples-FS26.git
cd DSaaP-examples-FS26/5_testing/unit_test_example_1

python3 -m venv gccontent
source gccontent/bin/activate
pip install -r requirements.txt
```

## Running the Script

To run the script, make sure to setup and activate the environment first:

```zsh
source gccontent/bin/activate
```

To run the script on a fasta file of your choosing:

```zsh
python gc_content/gc_content.py /path/to/fasta/file
```

To run the script on the example fasta file:

```zsh
python gc_content/gc_content.py data/DNA_example.fasta
```

The output of the script will be the GC contents for each sequence in the fasta file.

## Testing

To run unit tests:

```zsh
python -m unittest
```

### Test Coverage

To run unit tests with coverage and generate an html report, run:
```zsh
coverage run -m unittest
coverage html
```

## Data

The `data/` folder contains an example fasta file with DNA sequences.

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP) course, Spring semester 2026 (FS26).

## License

This project is licensed under the MIT License – see the LICENSE file for details.