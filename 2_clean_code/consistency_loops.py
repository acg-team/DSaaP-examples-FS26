# bad:
def count_high_expression_genes_bad(samples, threshold):
    total_count = 0

    i = 0
    while i < len(samples):
        for gene in samples[i].genes:
            if gene.expression_level > threshold:
                total_count += 1
        i += 1

    return total_count

# better:
def count_high_expression_genes_better(samples, threshold):
    total_count = 0

    for sample in samples:
        for gene in sample.genes:
            if gene.expression_level > threshold:
                total_count += 1

    return total_count

# good:
def count_high_expression_genes(samples, threshold):
    return sum(1 for sample in samples for gene in sample.genes if gene.expression_level > threshold)

    