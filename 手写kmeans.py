import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
from scipy.io import loadmat

def displayData(X, example_width=None, figsize=(10, 10)):
    """
    Displays 2D data in a nice grid.
    Parameters
    ----------
    X : array_like
        The input data of size (m x n) where m is the number of examples and n is the number of
        features.
    example_width : int, optional
        THe width of each 2-D image in pixels. If not provided, the image is assumed to be square,
        and the width is the floor of the square root of total number of pixels.
    figsize : tuple, optional
        A 2-element tuple indicating the width and height of figure in inches.
    """
    # Compute rows, cols
    if X.ndim == 2:
        m, n = X.shape
    elif X.ndim == 1:
        n = X.size
        m = 1
        X = X[None]  # Promote to a 2 dimensional array
    else:
        raise IndexError('Input X should be 1 or 2 dimensional.')

    example_width = example_width or int(np.round(np.sqrt(n)))
    example_height = int(n / example_width)

    # Compute number of items to display
    display_rows = int(np.floor(np.sqrt(m)))
    display_cols = int(np.ceil(m / display_rows))

    fig, ax_array = plt.subplots(display_rows, display_cols, figsize=figsize)
    fig.subplots_adjust(wspace=0.025, hspace=0.025)

    ax_array = [ax_array] if m == 1 else ax_array.ravel()

    for i, ax in enumerate(ax_array):
        ax.imshow(X[i].reshape(example_height, example_width, order='F'), cmap='gray')
        ax.axis('off')


def featureNormalize(X):
    """
    Normalizes the features in X returns a normalized version of X where the mean value of each
    feature is 0 and the standard deviation is 1. This is often a good preprocessing step to do when
    working with learning algorithms.
    Parameters
    ----------
    X : array_like
        An dataset which is a (m x n) matrix, where m is the number of examples,
        and n is the number of dimensions for each example.
    Returns
    -------
    X_norm : array_like
        The normalized input dataset.
    mu : array_like
        A vector of size n corresponding to the mean for each dimension across all examples.
    sigma : array_like
        A vector of size n corresponding to the standard deviations for each dimension across
        all examples.
    """
    mu = np.mean(X, axis=0)
    X_norm = X - mu

    sigma = np.std(X_norm, axis=0, ddof=1)
    X_norm /= sigma
    return X_norm, mu, sigma


def plotProgresskMeans(i, X, centroid_history, idx_history):
    """
    A helper function that displays the progress of k-Means as it is running. It is intended for use
    only with 2D data. It plots data points with colors assigned to each centroid. With the
    previous centroids, it also plots a line between the previous locations and current locations
    of the centroids.
    Parameters
    ----------
    i : int
        Current iteration number of k-means. Used for matplotlib animation function.
    X : array_like
        The dataset, which is a matrix (m x n). Note since the plot only supports 2D data, n should
        be equal to 2.
    centroid_history : list
        A list of computed centroids for all iteration.
    idx_history : list
        A list of computed assigned indices for all iterations.
    """
    K = centroid_history[0].shape[0]
    plt.gcf().clf()
    cmap = plt.cm.rainbow
    norm = matplotlib.colors.Normalize(vmin=0, vmax=2)

    for k in range(K):
        current = np.stack([c[k, :] for c in centroid_history[:i + 1]], axis=0)
        plt.plot(current[:, 0], current[:, 1],
                 '-Xk',
                 mec='k',
                 lw=2,
                 ms=10,
                 mfc=cmap(norm(k)),
                 mew=2)

        plt.scatter(X[:, 0], X[:, 1],
                    c=idx_history[i],
                    cmap=cmap,
                    marker='o')
    plt.grid(False)
    plt.title('Iteration number %d' % (i + 1))


def runkMeans(X, K):

    centroids = kMeansInitCentroids(X, K)

    for i in range(20):
        idx = findClosestCentroids(X, centroids)
        centroids = computeCentroids(X, idx, K)

    return centroids, idx


def findClosestCentroids(X, centroids):

    K = centroids.shape[0]


    idx = np.zeros(X.shape[0])


    for i in range(X.shape[0]):
        idx[i] = np.argmin(np.sum((X[i, :] - centroids) ** 2, axis=1))

    return idx


def computeCentroids(X, idx, K):

    m, n = X.shape

    centroids = np.zeros((K, n))


    for i in range(K):
        centroids[i, :] = np.mean(X[idx == i], axis=0)

    return centroids


def kMeansInitCentroids(X, K):

    m, n = X.shape

    choice = np.random.permutation(m)[:K]
    centroids = X[choice]

    return centroids


if __name__ == '__main__':
    initial_centroids = [[3, 3], [6, 2], [8, 5]]

    data = []
    data += [[initial_centroids[0][0] + np.random.randn() * 0.8, initial_centroids[0][1] +  np.random.randn() * 0.8] for _ in range(50)]
    data += [[initial_centroids[1][0] + np.random.randn() * 0.8, initial_centroids[1][1] +  np.random.randn() * 0.8] for _ in range(50)]
    data += [[initial_centroids[2][0] + np.random.randn() * 0.8, initial_centroids[2][1] +  np.random.randn() * 0.8] for _ in range(50)]

    m = len(data)
    data = np.array(data)
    data = data[np.random.permutation(m)]

    print(data.shape)
    plt.scatter(data[:, 0], data[:, 1])
    plt.show()

    centroids, idx = runkMeans(data, 3)
    print(centroids)
    print(idx)

    print(data[idx == 0])
    plt.scatter(data[idx == 0][:, 0], data[idx == 0][:, 1], c='r')
    plt.scatter(data[idx == 1][:, 0], data[idx == 1][:, 1], c='g')
    plt.scatter(data[idx == 2][:, 0], data[idx == 2][:, 1], c='b')

    plt.show()
