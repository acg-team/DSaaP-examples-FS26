def select_differential_expression_samples(samples, min_reads, min_quality):
    # Select samples with sufficient sequencing depth (minimal number of reads)
    # and technical quality for downstream differential expression analysis.

    eligible_samples = []

    for sample in samples:
        if sample.read_count > min_reads and sample.quality_score > min_quality:
            eligible_samples.append(sample)

    return eligible_samples
