class Gene:
    id = None

    def __init__(self, id):
        self.id = id

# buggy:


def contains_gene_bugged(genes, target_id):
    result = False
    for gene in genes:
        if gene.id == target_id:
            result = True
        break
    return result

# fixed:


def contains_gene_fixed(genes, target_id):
    result = False
    for gene in genes:
        if gene.id == target_id:
            result = True
            break
    return result

# better:


def contains_gene_better(genes, target_id):
    for gene in genes:
        if gene.id == target_id:
            return True
    return False


if __name__ == "__main__":
    genes = [Gene("gene1"), Gene("gene2"), Gene("gene3")]

    print("Should be True:")
    print(contains_gene_bugged(genes, "gene1"))
    print(contains_gene_fixed(genes, "gene1"))
    print(contains_gene_better(genes, "gene1"))

    print("Should be True:")
    print(contains_gene_bugged(genes, "gene2"))
    print(contains_gene_fixed(genes, "gene2"))
    print(contains_gene_better(genes, "gene2"))

    print("Should be False:")
    print(contains_gene_bugged(genes, "gene4"))
    print(contains_gene_fixed(genes, "gene4"))
    print(contains_gene_better(genes, "gene4"))
