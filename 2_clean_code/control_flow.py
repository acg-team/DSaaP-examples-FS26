def compute_expression(sample):
    return sum(g.expression_level for g in sample.genes) / len(sample.genes)


# bad:
def sample_expression_bad(sample, threshold):
    if sample is not None:
        if sample.has_reads():
            if sample.quality_score > threshold:
                return compute_expression(sample)
    return None


# better:
def sample_expression(sample, threshold):
    if sample is None:
        return None

    if not sample.has_reads():
        return None

    if sample.quality_score <= threshold:
        return None

    return compute_expression(sample)
