import numpy as np
from typing import Tuple
from scipy.fft import fft, ifft


class FourierDescriptors2D:
    def __init__(self, num_descriptors: int):
        self.num_descriptors = num_descriptors
        self.a = None
        self.b = None

    def fit_transform(self, curve: np.ndarray) -> np.ndarray:
        self.a, self.b = self.compute_coefficients(curve)
        return np.column_stack((self.a[:self.num_descriptors], self.b[:self.num_descriptors]))

    def inverse_transform(self, fd_coeffs: np.ndarray) -> np.ndarray:
        a_padded = np.pad(fd_coeffs[:, 0], (0, len(self.a) - self.num_descriptors), 'constant')
        b_padded = np.pad(fd_coeffs[:, 1], (0, len(self.b) - self.num_descriptors), 'constant')
        a_padded[0] /= 2
        a_padded[self.num_descriptors:] = 0
        b_padded[self.num_descriptors:] = 0
        a_full = np.concatenate((a_padded, a_padded[-2:0:-1]))
        b_full = np.concatenate((b_padded, -b_padded[-2:0:-1]))
        return np.column_stack((np.fft.ifft(a_full + 1j * b_full).real, np.fft.ifft(a_full - 1j * b_full).real))

    def compute_coefficients(self, curve: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        n = curve.shape[0]
        t = np.arange(n)
        z = curve[:, 0] + 1j * curve[:, 1]
        a = np.fft.fft(z).real / n
        b = np.fft.fft(z).imag / n
        a[0] /= 2
        a[1:] *= 2
        b[1:] *= -2
        return a, b

class FourierDescriptors:
    def __init__(self, num_descriptors=10):
        self.num_descriptors = num_descriptors
    
    def fit_transform(self, curve):
        assert curve.ndim >= 2, "Curve must be a 2D array or higher"
        assert curve.shape[-1] > 1, "Curve must have more than one dimension"
        assert self.num_descriptors < curve.shape[0]//2, "Number of descriptors must be less than half the number of points in the curve"
        
        N = curve.shape[0]
        T = 1/N
        t = np.linspace(0, 1-T, N)

        # Calculate Fourier coefficients
        c = fft(curve, axis=0)
        c = np.vstack((c[:self.num_descriptors], np.zeros_like(c[self.num_descriptors:]), c[-self.num_descriptors:]))
        
        # Inverse transform to obtain descriptors
        descriptors = ifft(c, axis=0).real

        # Compute magnitudes of descriptors
        magnitudes = np.sqrt((descriptors ** 2).sum(axis=-1))
        magnitudes[..., 0] /= 2

        # Normalize descriptors
        descriptors /= magnitudes[..., None]

        # Save magnitudes and descriptors for inverse transform
        self.magnitudes_ = magnitudes
        self.descriptors_ = descriptors

        return descriptors.reshape(-1)
    
    def inverse_transform(self, descriptors):
        assert descriptors.ndim == 1, "Descriptors must be a 1D array"
        assert descriptors.shape[0] == 2*self.num_descriptors+1, "Number of descriptors does not match"
        
        c = descriptors.reshape(-1, 1, 1) * self.descriptors_
        curve = np.real(ifft(c, axis=0))

        return curve
