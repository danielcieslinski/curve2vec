import sys

# Add the parent directory to the Python path
sys.path.insert(0, 'src/')

import numpy as np
from curve2vec.embeddings.fourier import FourierDescriptors
from curve2vec.utils.data import circle

def test_fourier_descriptors():
    # Test circle curve
    curve = circle(100)
    fd = FourierDescriptors(num_descriptors=10)
    fd_coeffs = fd.fit_transform(curve)
    print()
    print(len(fd_coeffs))
    reconstructed_curve = fd.inverse_transform(fd_coeffs)
    #print(curve)
    # print(reconstructed_curve)
    assert np.allclose(curve, reconstructed_curve, rtol=1e-3, atol=1e-3)

    # Test random curve
    curve = np.random.randn(100, 9)
    fd = FourierDescriptors(num_descriptors=10)
    fd_coeffs = fd.fit_transform(curve)
    reconstructed_curve = fd.inverse_transform(fd_coeffs)
    assert np.allclose(curve, reconstructed_curve, rtol=1e-3, atol=1e-3)

    # Test for correct number of coefficients
    curve = circle(100)
    fd = FourierDescriptors(num_descriptors=10)
    fd_coeffs = fd.fit_transform(curve)
    assert fd_coeffs.shape[0] == fd.num_descriptors

test_fourier_descriptors()