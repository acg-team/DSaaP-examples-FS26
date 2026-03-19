import pytest
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from gc_content.gc_content import calculate_gc_content

def test_empty_sequence():
    # Edge case: empty sequence
    record = SeqRecord(Seq(""), id="seq1")
    assert calculate_gc_content(record) == 0.0

def test_no_gc():
    # Edge case: sequence with no G or C
    record = SeqRecord(Seq("ATAT"), id="seq2")
    assert calculate_gc_content(record) == pytest.approx(0.0)

def test_all_gc():
    # 100% GC
    record = SeqRecord(Seq("GGCC"), id="seq3")
    assert calculate_gc_content(record) == pytest.approx(1.0)

def test_simple_sequence():
    # 50% GC
    record = SeqRecord(Seq("ATGC"), id="seq4")
    assert calculate_gc_content(record) == pytest.approx(0.5)

def test_only_g():
    # 100% G
    record = SeqRecord(Seq("GGGG"), id="seq5")
    assert calculate_gc_content(record) == pytest.approx(1.0)

def test_only_c():
    # 100% C
    record = SeqRecord(Seq("AAACCC"), id="seq6")
    assert calculate_gc_content(record) == pytest.approx(0.5)

def test_mixed_case():
    # 6/10 = 0.6 GC content, case insensitivity check
    record = SeqRecord(Seq("atgcGGGCAT"), id="seq7")
    assert calculate_gc_content(record) == pytest.approx(0.6)

def test_strong_nucleotides():
    # 'S' is considered as G or C, so GC content should be 5/9 = 0.555...
    record = SeqRecord(Seq("AATTGGCCS"), id="seq8")
    assert calculate_gc_content(record) == pytest.approx(5/9)

