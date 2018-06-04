import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import mutation_waterfall.preprocess as preprocess


def plot(mutation_list_file, n_genes=30, ax=None, file=None):
    """Generates a waterfall plot describing mutational landscape of samples.

    Args:
        mutation_list_file: Path to mutation list.
        num_gene: Number of genes to be plotted. (default: 30)
        ax: Matplotlib axis to draw the plot.
        file: If not None, resulting plot will be saved as an image file.

    Returns:
        ax: Axis containing the plot.
    """
    binary_matrix, genes, samples = preprocess.make_binary_matrix(mutation_list_file)

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
    plt.sca(ax)

    waterfall(binary_matrix, genes, n_genes, ax)

    plt.tight_layout()
    if file:
        plt.savefig(file, dpi=150)
    else:
        plt.show()


def waterfall(binary_matrix, genes, num_gene, ax):
    """Sort binary matrix and plot it.

    Args:
        binary_matrix: Binary matrix containing mutation status.
        genes: List of genes.
        num_gene: Number of genes to be plotted.
        ax: Matplotlib axis to draw the plot.

    Returns:
        ax: Axis containing the plot.
    """
    row_order = binary_matrix.sum(axis=1).argsort()[::-1]
    temp = binary_matrix[row_order]

    column_order = np.array([''.join([str(x) for j, x in enumerate(temp[:, i])]) for i in range(temp.shape[1])]).argsort()[::-1]
    temp = temp[:, column_order]

    # Y-axis tick labels
    ax.set_yticks(np.arange(num_gene))
    percentages = binary_matrix.sum(axis=1) / binary_matrix.shape[1] * 100
    yticklabels = ['$%s$ (%.1f%%)' % (genes[ix], percentages[ix]) for ix in row_order[:num_gene]]
    plt.yticks(np.arange(num_gene), yticklabels)

    ax.set_xticks(np.arange(-.5, temp.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-.5, num_gene, 1), minor=True)
    ax.grid(which='minor', color='grey', linestyle='-', alpha=0.33, linewidth=1,)

    plt.xticks([])
    ax.imshow(temp[:num_gene, :], interpolation='none', aspect='auto', cmap=plt.cm.gray_r)

    return ax
