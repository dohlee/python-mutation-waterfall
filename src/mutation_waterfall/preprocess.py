import pandas as pd
import numpy as np


def make_binary_matrix(mutation_list_file):
    """Makes binary matrix from muation list file.

    Mutation list file should be formatted like below:
    ---
    Sample  Mutation
    S1  GeneA
    S1  GeneB
    S2  GeneA
    S2  GeneC
    S3  GeneD
    ---

    Args:
        mutation_list_file: Path to the mutation list file.

    Returns:
        binary_matrix: Binarized mutation-sample matrix.
            Each row indicates a gene, and each column indicates a sample.
        genes: List of genes.
        samples: List of samples.
    """
    mutation_df = pd.read_csv(mutation_list_file, skiprows=1, names=['Sample', 'Mutation'], sep='\t')
    genes = mutation_df.Mutation.unique()
    samples = mutation_df.Sample.unique()

    sample_gene_dict = dict()
    for sample in samples:
        mutation_per_sample = mutation_df[mutation_df.Sample == sample].Mutation.values
        sample_gene_dict[sample] = set(mutation_per_sample)

    binary_matrix = np.zeros([len(genes), len(samples)])
    for i, gene in enumerate(genes):
        for j, sample in enumerate(samples):
            if gene in sample_gene_dict[sample]:
                binary_matrix[i, j] = 1

    return binary_matrix, genes, samples
