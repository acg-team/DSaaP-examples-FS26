import unittest
from unittest.mock import patch
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from gc_content.gc_content import calculate_gc_content, read_sequences_from_file, main


class TestGCContent(unittest.TestCase):

    def test_empty_sequence(self):
        # Edge case: empty string
        record = SeqRecord(Seq(""), id="seq1")
        self.assertEqual(calculate_gc_content(record), 0.0)

    def test_no_gc(self):
        # Edge case: sequence with no G or C
        record = SeqRecord(Seq("ATAT"), id="seq2")
        self.assertAlmostEqual(calculate_gc_content(record), 0.0)

    def test_all_gc(self):
        # 100% GC
        record = SeqRecord(Seq("GGCC"), id="seq3")
        self.assertAlmostEqual(calculate_gc_content(record), 1.0)

    def test_simple_sequence(self):
        # 50% GC
        record = SeqRecord(Seq("ATGC"), id="seq4")
        self.assertAlmostEqual(calculate_gc_content(record), 0.5)

    def test_only_g(self):
        # 100% G
        record = SeqRecord(Seq("GGGG"), id="seq5")
        self.assertAlmostEqual(calculate_gc_content(record), 1.0)

    def test_only_c(self):
        # 100% C
        record = SeqRecord(Seq("AAACCC"), id="seq6")
        self.assertAlmostEqual(calculate_gc_content(record), 0.5)

    def test_mixed_case(self):
        # 4/8 = 0.5
        record = SeqRecord(Seq("atgcATGC"), id="seq7")
        self.assertAlmostEqual(calculate_gc_content(record), 0.5)

    def test_strong_nucleotides(self):
        # Case insensitivity check
        # 'S' is considered as G or C, so 5/9 = 0.555...
        record = SeqRecord(Seq("AATTGGCCS"), id="seq8")
        self.assertAlmostEqual(calculate_gc_content(record), 5/9)

if __name__ == '__main__':
    unittest.main()
