from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from gc_content.gc_content import read_sequences_from_file

def test_read_sequences_file_not_found():
    # Test that the function returns an empty list when the file is not found
    result = read_sequences_from_file("non_existent_file.fasta")
    assert result == []

def test_read_sequences_non_fasta():
    # Test that the function returns an empty list when the file is not a FASTA file
    result = read_sequences_from_file("test/data/non_fasta.phy")
    assert result == []

def test_read_sequences_empty_file():
    # Test that the function returns an empty list when the file is empty
    result = read_sequences_from_file("test/data/empty.fasta")
    assert result == []

def test_read_sequences_mocked(mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    mock_parse = mocker.patch('Bio.SeqIO.parse')

    # Prepare mock data
    # SeqIO.parse yields SeqRecord objects
    mock_record1 = SeqRecord(Seq("ATGC"), id="seq1")
    mock_record2 = SeqRecord(Seq("CGTA"), id="seq2")

    # Configure the mock to return an iterator of our mock records
    mock_parse.return_value = iter([mock_record1, mock_record2])

    # Call the function
    file_path = "dummy.fasta"
    result = read_sequences_from_file(file_path)

    # Assertions
    # Expect list of SeqRecord objects. Check sequence strings.
    assert [str(r.seq) for r in result] == ["ATGC", "CGTA"]

    # Verify open was called
    mock_open.assert_called_once_with(file_path, "r")

    # Verify SeqIO.parse was called with correct arguments
    mock_parse.assert_called_once_with(mock_open.return_value, "fasta-pearson")

def test_read_sequences_generic_exception(mocker):
    mock_open = mocker.patch('builtins.open')
    # Configure the mock to raise a generic Exception
    mock_open.side_effect = Exception("Generic error")

    # Call the function
    result = read_sequences_from_file("dummy.fasta")

    # Assertions
    assert result == []

