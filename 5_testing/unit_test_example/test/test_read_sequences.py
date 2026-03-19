from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from gc_content.gc_content import read_sequences_from_file

def test_read_sequences_file_not_found():
    # Function returns an empty list when the file is not found
    result = read_sequences_from_file("non_existent_file.fasta")
    assert result == []

def test_read_sequences_non_fasta():
    # Function returns an empty list when the file is not a FASTA file
    result = read_sequences_from_file("test/data/non_fasta.phy")
    assert result == []

def test_read_sequences_empty_file():
    # Function returns an empty list when the file is empty
    result = read_sequences_from_file("test/data/empty.fasta")
    assert result == []

def test_read_sequences_valid():
    # Function returns a list of SeqRecord objects when the file is valid
    result = read_sequences_from_file("test/data/DNA_short.fasta")
    assert len(result) == 4
    assert result[0].id == "A"
    assert str(result[0].seq) == "CTGTTCA"
    assert result[1].id == "B"
    assert str(result[1].seq) == "CTGTT"
    assert result[2].id == "C"
    assert str(result[2].seq) == "CTCTT"
    assert result[3].id == "D"
    assert str(result[3].seq) == "GTCTA"

def test_read_sequences_mocked(mocker):
    # Mock file open
    mock_open = mocker.patch('builtins.open', mocker.mock_open())

    # Mock SeqIO.parse to return an iterator of SeqRecords
    mock_parse = mocker.patch('Bio.SeqIO.parse')
    mock_record1 = SeqRecord(Seq("ATGC"), id="seq1")
    mock_record2 = SeqRecord(Seq("CGTA"), id="seq2")
    mock_parse.return_value = iter([mock_record1, mock_record2])

    file_path = "dummy.fasta"
    result = read_sequences_from_file(file_path)

    assert result == [mock_record1, mock_record2]

    # Verify open was called
    mock_open.assert_called_once_with(file_path, "r")

    # Verify SeqIO.parse was called with correct arguments
    mock_parse.assert_called_once_with(mock_open.return_value, "fasta-pearson")

def test_read_sequences_generic_exception(mocker):
    # Mock file open
    mock_open = mocker.patch('builtins.open')

    # Configure the mock to raise a generic Exception
    mock_open.side_effect = Exception("Generic error")

    result = read_sequences_from_file("dummy.fasta")

    assert result == []

