from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from gc_content.gc_content import main

def test_main(mocker):
    mock_calculate = mocker.patch('gc_content.gc_content.calculate_gc_content')
    mock_read = mocker.patch('gc_content.gc_content.read_sequences_from_file')
    mock_print = mocker.patch('builtins.print')
    mock_parse_args = mocker.patch('argparse.ArgumentParser.parse_args')

    # Set up mock arguments
    mock_parse_args.return_value.file_path = "dummy.fasta"

    # Set up mock return values
    record = SeqRecord(Seq("ATGC"), id="seq1")
    mock_read.return_value = [record]
    mock_calculate.return_value = 0.5

    # Call the main function
    main()

    # Check that read_sequences_from_file was called with the correct argument
    mock_read.assert_called_once_with("dummy.fasta")

    # Check that calculate_gc_content was called
    mock_calculate.assert_called_once_with(record)

    # Check that the output was printed
    mock_print.assert_called_once_with(">seq1\nGC content: 50.00%")

def test_main_empty(mocker):
    mock_calculate = mocker.patch('gc_content.gc_content.calculate_gc_content')
    mock_read = mocker.patch('gc_content.gc_content.read_sequences_from_file')
    mock_print = mocker.patch('builtins.print')
    mock_parse_args = mocker.patch('argparse.ArgumentParser.parse_args')

    # Set up mock arguments
    mock_parse_args.return_value.file_path = "dummy.fasta"

    # Set up mock return values
    mock_read.return_value = []
    mock_calculate.return_value = 0.0

    # Call the main function
    main()

    # Check that read_sequences_from_file was called with the correct argument
    mock_read.assert_called_once_with("dummy.fasta")

    # Check that calculate_gc_content was not called since there are no sequences
    mock_calculate.assert_not_called()

    # Check that nothing was printed
    mock_print.assert_not_called()

