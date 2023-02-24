import sys

# Add the parent directory to the Python path
sys.path.insert(0, 'src/')

import numpy as np
from curve2vec.embeddings.fourier import FourierDescriptors
from curve2vec.utils.data import circle

def test_fourier_descriptors():
    # Test circle curve
    curve = circle(100)
    fd = FourierDescriptors(order=10)
    fd_coeffs = fd.fit_transform([curve])
    reconstructed_curve = fd.reconstruct(fd_coeffs)
    assert np.allclose(curve, reconstructed_curve, rtol=1e-3, atol=1e-3)

    # Fourier descriptors work only for closed curves
    # Test random curve
    curve = np.random.randn(100, 2)
    fd = FourierDescriptors(order=10)
    fd_coeffs = fd.fit_transform([curve])
    reconstructed_curve = fd.reconstruct(fd_coeffs)
    # assert np.allclose(curve, reconstructed_curve, rtol=1e-2, atol=1e-2)

test_fourier_descriptors()