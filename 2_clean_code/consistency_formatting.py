#bad:
def getGenes(sample):
    gene_list = []
    for g in sample.genes:
        if g.ExprLevel > 5:
            gene_list.append(g)
    return gene_list


# better:
def get_genes_above_threshold(sample, threshold):
    selected_genes = []

    for gene in sample.genes:
        if gene.expression_level > threshold:
            selected_genes.append(gene)

    return selected_genes