import numpy as np
from pyefd import elliptic_fourier_descriptors, normalize_efd, reconstruct_contour

class FourierDescriptors:
    def __init__(self, order=10, normalize=False, size_invariant=True):
        self.order = order
        self.normalize = normalize
        self.size_invariant = size_invariant
        self.coeffs = None

    def fit(self, X):
        self.coeffs = np.array([elliptic_fourier_descriptors(contour, self.order, self.normalize) for contour in X])
        if self.size_invariant:
            self.coeffs = np.array([normalize_efd(coeffs) for coeffs in self.coeffs])

    def transform(self, X):
        return np.array([elliptic_fourier_descriptors(contour, self.order, self.normalize) for contour in X])

    def fit_transform(self, X):
        self.fit(X)
        return self.coeffs

    def reconstruct(self, X, locus=(0,0), num_points=100):
        return np.array([reconstruct_contour(coeffs, locus=locus, num_points=num_points) for coeffs in X])