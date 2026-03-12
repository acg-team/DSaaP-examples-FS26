# bad:
def analyse_bad(sample, threshold, filename):
    selected = []
    for gene in sample.genes:
        if gene.expression_level > threshold:
            selected.append(gene)

    if not selected:
        print("No genes passed the threshold.")
        return None

    mean = sum(g.expression_level for g in selected) / len(selected)

    with open(filename, "w") as f:
        for gene in selected:
            f.write(gene.id + "\n")

    print("Mean expression:", mean)

    return mean

# better:
def filter_expressed_genes(genes, threshold):
    return [g for g in genes if g.expression_level > threshold]


def get_mean_expression(genes):
    return sum(g.expression_level for g in genes) / len(genes)


def save_ids_to_file(genes, filename):
    with open(filename, "w") as f:
        f.writelines([g.id + "\n" for g in genes])


def analyse(sample, threshold, filename):
    selected = filter_expressed_genes(sample.genes, threshold)
    if not selected:
        return None

    save_ids_to_file(selected, filename)

    return get_mean_expression(selected)