def filter_low_quality_reads(reads):
    high_quality_reads = []

    for read in reads:
        if read.quality_score > 20:  # filter reads above quality 30
            high_quality_reads.append(read)

    return high_quality_reads
