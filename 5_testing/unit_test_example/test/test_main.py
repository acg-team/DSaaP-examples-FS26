import pytest
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from gc_content.gc_content import main

@pytest.fixture
def mock_deps(mocker):
    mock_parse_args = mocker.patch('argparse.ArgumentParser.parse_args')
    mock_parse_args.return_value.file_path = "dummy.fasta"

    return {
        'parse_args': mock_parse_args,
        'read': mocker.patch('gc_content.gc_content.read_sequences_from_file'),
        'calculate': mocker.patch('gc_content.gc_content.calculate_gc_content'),
        'print': mocker.patch('builtins.print')
    }

def test_main(mock_deps):
    # Mock read_sequences_from_file to return a list of SeqRecord objects
    mock_record = SeqRecord(Seq("ATGC"), id="seq1")
    mock_deps['read'].return_value = [mock_record]

    # Mock calculate_gc_content to return a specific value
    mock_deps['calculate'].return_value = 0.5

    main()

    # Check that read_sequences_from_file was called with the correct argument
    mock_deps['read'].assert_called_once_with("dummy.fasta")

    # Check that calculate_gc_content was called once with the correct argument
    mock_deps['calculate'].assert_called_once_with(mock_record)

    # Check that the correct output was printed
    mock_deps['print'].assert_called_once_with(">seq1\nGC content: 50.00%")

def test_main_empty(mock_deps):
    # Set up mock return values
    mock_deps['read'].return_value = []
    mock_deps['calculate'].return_value = 0.0

    # Call the main function
    main()

    # Check that read_sequences_from_file was called with the correct argument
    mock_deps['read'].assert_called_once_with("dummy.fasta")

    # Check that calculate_gc_content was not called since there are no sequences
    mock_deps['calculate'].assert_not_called()

    # Check that nothing was printed
    mock_deps['print'].assert_not_called()
