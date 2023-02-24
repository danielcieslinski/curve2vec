import matplotlib.pyplot as plt
import numpy as np

def plot_curve(curve):
    """
    Plots a closed curve as a matplotlib figure.

    Parameters:
        curve (ndarray): A numpy array of (x,y) coordinates representing the curve.

    Returns:
        None
    """
    plt.figure()
    plt.plot(curve[:, 0], curve[:, 1], 'b-', linewidth=2)
    plt.axis('equal')
    plt.show()

def plot_embedding(curve, embedding):
    """
    Plots a curve and its embedding as a matplotlib figure.

    Parameters:
        curve (ndarray): A numpy array of (x,y) coordinates representing the curve.
        embedding (ndarray): A numpy array representing the embedding of the curve.

    Returns:
        None
    """
    plt.figure()
    plt.subplot(121)
    plt.plot(curve[:, 0], curve[:, 1], 'b-', linewidth=2)
    plt.axis('equal')
    plt.title('Original Curve')
    plt.subplot(122)
    plt.plot(np.real(embedding), np.imag(embedding), 'r.')
    plt.axis('equal')
    plt.title('Embedding')
    plt.show()

def plot_curves(curves):
    """
    Plots a list of curves as a matplotlib figure.

    Parameters:
        curves (list): A list of numpy arrays of (x,y) coordinates representing the curves.

    Returns:
        None
    """
    num_curves = len(curves)
    # fig, axes = plt.subplots(nrows=1, ncols=num_curves, figsize=(3*num_curves, 3))
    for i in range(num_curves):
        plt.plot(curves[i][:, 0], curves[i][:, 1], linewidth=2, label=i)
        plt.axis('equal')
    
    plt.legend()
    plt.show()