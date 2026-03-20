# GC Content of Sequences

This is a basic Python script to calculate GC content from sequences in a fasta file. The setup is the same as in `unit_test_example`, but the test suite is shortened and a bug is introduced to show how full code coverage is not enough to make sure the code runs correctly.

## Setup

To run these examples, you need Python 3 installed and a clone of the [DSaaP examples repository]( https://github.com/acg-team/DSaaP-examples-FS26 ).

You can use a virtual environment to install dependencies:

```zsh
# Clone the repository if you haven't already
# git clone git@github.com:acg-team/DSaaP-examples-FS26.git
# cd DSaaP-examples-FS26/5_testing/unit_test_example_full_coverage_mutant

# Create and activate virtual environment
python3 -m venv gcc_venv
source gcc_venv/bin/activate

# Install dependencies (biopython, coverage, pytest, pytest-mock)
pip install -r requirements.txt
```

Alternatively, you can install the dependencies system-wide:
```zsh
pip install -r requirements.txt
```

## Running the Script

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
pytest test
```

### Test Coverage

To run unit tests with coverage and generate an html report, run:
```zsh
coverage run -m pytest
coverage html
```

To view the coverage report in your browser you can run:
```zsh
open htmlcov/index.html
```

## Data

The `data/` folder contains an example fasta file with DNA sequences.

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP) course, Spring semester 2026 (FS26).

## License

This project is licensed under the MIT License – see the LICENSE file for details.