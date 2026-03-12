# bad:
def compute_mean_expression_bad(sample, threshold):
    mean = None

    if sample is not None:
        if sample.passed_qc:
            if len(sample.genes) > 0:
                selected = []

                for gene in sample.genes:
                    if gene.expression_level > threshold:
                        selected.append(gene)

                if len(selected) > 0:
                    total = 0
                    for g in selected:
                        total += g.expression_level

                    mean = total / len(selected)

    return mean


# better:
def compute_mean_expression(sample, threshold):
    if sample is None:
        return None

    if not sample.passed_qc:
        return None

    if not sample.genes:
        return None

    selected = [
        gene.expression_level
        for gene in sample.genes
        if gene.expression_level > threshold
    ]

    if not selected:
        return None

    return sum(selected) / len(selected)