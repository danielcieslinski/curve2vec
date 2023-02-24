import numpy as np
from curve2vec.utils import visualization
from curve2vec.utils.data import generate_random_walk_curves

# Test visualize.py
# Generate a random curve
curve = np.random.randn(100, 2)
# Plot the curve
visualization.plot_curve(curve)

# Test data.py
# Generate 10 random walk curves
curves = generate_random_walk_curves(num_curves=10, num_points=100)
# Plot all the curves on the same plot
visualization.plot_curves(curves)
