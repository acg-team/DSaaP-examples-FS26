# bad:
def compute_mean_expression_bad(sample):
    total = sum(g.expression for g in sample.genes)

    # old version:
    # mean = total / 100

    mean = total / len(sample.genes)
    return mean

# better:
def compute_mean_expression(sample):
    total = sum(g.expression for g in sample.genes)
    mean = total / len(sample.genes)
    return mean