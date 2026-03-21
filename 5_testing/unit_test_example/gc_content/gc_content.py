from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from collections.abc import Sequence
import argparse
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def calculate_gc_content(record: SeqRecord) -> float:
    """
    Calculates the GC content of a DNA sequence.

    Args:
        record (SeqRecord): The DNA sequence record.

    Returns:
        float: The fraction of G and C bases in the sequence (0.0 to 1.0).
        0.0 if the sequence is empty.

    Example:
    >>> from Bio.SeqRecord import SeqRecord, Seq
    >>> calculate_gc_content(SeqRecord(Seq("AGCTASSTTA")))
    0.4
    """
    if not record.seq:
        return 0.0

    sequence = record.seq.upper()  # Ensure sequence is uppercase for counting
    gc_count = sequence.count('G') + sequence.count('C') + sequence.count('S')
    return gc_count / len(sequence)


def read_sequences_from_file(file_path: str) -> list[SeqRecord]:
    """
    Reads sequences from a FASTA file using Biopython.

    Args:
        file_path (str): Path to the FASTA file.

    Returns:
        list[SeqRecord]: A list of SeqRecord objects.
    """
    sequences = []
    try:
        logger.info(f"Reading sequences from {file_path}")
        with open(file_path, "r") as handle:
            for record in SeqIO.parse(handle, "fasta-pearson"):
                sequences.append(record)
        if len(sequences) == 0:
            logger.warning(f"No sequences found in {file_path}")
        else:
            logger.info(f"Successfully read {len(sequences)} sequences from {file_path}")
    except FileNotFoundError:
        logger.error(f"File not found at {file_path}")
        return []
    except Exception as e:
        logger.exception(f"Error reading file: {e}")
        return []

    return sequences


def main():
    parser = argparse.ArgumentParser(
        description="Calculate GC content for each sequence in a FASTA file."
    )
    parser.add_argument("file_path", help="Path to the FASTA file.")
    args = parser.parse_args()

    sequences = read_sequences_from_file(args.file_path)

    for record in sequences:
        gc_content = calculate_gc_content(record)
        print(f">{record.id}\nGC content: {gc_content:.2%}")


if __name__ == '__main__':
    main()
