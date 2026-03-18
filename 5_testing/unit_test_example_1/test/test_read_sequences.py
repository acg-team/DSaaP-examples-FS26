import unittest
from unittest.mock import patch
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from gc_content.gc_content import read_sequences_from_file


class TestReadSequences(unittest.TestCase):

    def test_read_sequences_file_not_found(self):
        # Test that the function returns an empty list when the file is not found
        result = read_sequences_from_file("non_existent_file.fasta")
        self.assertEqual(result, [])

    def test_read_sequences_non_fasta(self):
        # Test that the function returns an empty list when the file is not a FASTA file
        result = read_sequences_from_file("data/non_fasta.phy")
        self.assertEqual(result, [])

    def test_read_sequences_empty_file(self):
        # Test that the function returns an empty list when the file is empty
        result = read_sequences_from_file("data/empty.fasta")
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('Bio.SeqIO.parse')
    def test_read_sequences_mocked(self, mock_parse, mock_open):
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
        self.assertEqual([str(r.seq) for r in result], ["ATGC", "CGTA"])

        # Verify open was called
        mock_open.assert_called_once_with(file_path, "r")

        # Verify SeqIO.parse was called with correct arguments
        mock_parse.assert_called_once_with(mock_open.return_value, "fasta-pearson")

    @patch('builtins.open')
    def test_read_sequences_generic_exception(self, mock_open):
        # Configure the mock to raise a generic Exception
        mock_open.side_effect = Exception("Generic error")

        # Call the function
        result = read_sequences_from_file("dummy.fasta")

        # Assertions
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
