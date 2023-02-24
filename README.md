# curve2vec

curve2vec is a Python library that provides various algorithms for creating vector embeddings of closed curves.

### Installation

You can install curve2vec using pip:

`pip install curve2vec`

### Usage

Here's an example of how to use curve2vec to create a Fourier descriptor embedding of a curve:

```py
import curve2vec.embeddings.fourier as fourier

# create a closed curve as a numpy array of (x,y) coordinates
curve = ...

# create a Fourier descriptor embedding of the curve
embedding = fourier.descriptor(curve, num_coeff=10)

print(embedding)
```

### Supported algorithms

curve2vec supports the following curve embedding algorithms:

- Fourier descriptors: Lossless embedding suitable for reconstructing the original curve. Good for curves with smooth, regular shapes.
- Continuous wavelet transform: Non-linear embedding that may result in information loss. Good for curves with local, non-uniform features.
- Shape context: Lossless embedding suitable for reconstructing the original curve. Good for curves with distinctive, repeated features.
- Curvature scale space: Lossless embedding suitable for reconstructing the original curve. Good for curves with sharp, angular features.
- Fractal dimension: Lossless embedding suitable for reconstructing the original curve. Good for curves with self-similar, fractal properties.
- Convolutional neural network: Non-linear embedding that may result in information loss. Good for curves with complex, irregular shapes.
- Long short-term memory neural network: Non-linear embedding that may result in information loss. Good for curves with sequential, time-dependent features.
- Symbolic aggregate approximation: Non-linear embedding that may result in information loss. Good for curves with distinctive, repeated patterns.

### Contributing

Contributions to curve2vec are welcome! If you find a bug or would like to propose a new feature or algorithm, please submit an issue or pull request on GitHub.

### License

curve2vec is licensed under the MIT License. See LICENSE for more information.
