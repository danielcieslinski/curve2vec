# Curve2Vec
Curve2Vec is a Python package for computing vector embeddings of curves. The resulting embeddings can be used for tasks such as clustering, classification, and similarity search. The package is in its early stage and is under active development.

## Installation
The package can be installed via pip:

`pip install curve2vec`

## Usage
### Extracting Features
At the moment the only available method for extraction are FourierDescriptors. First create a FourierDescriptors object, which is used to specify the order of the Fourier descriptors and other options:

```py
from curve2vec.embeddings.fourier import FourierDescriptors

fd = FourierDescriptors(order=20, normalize=True, size_invariant=True)
```

Once you have created the FourierDescriptors object, you can use its fit_transform method to extract features from a set of curves:

```py
import numpy as np

# X is a numpy array of curves, where each curve is an array of 2D points
X = np.array([...])

# Extract features from curves using Fourier descriptors
features = fd.fit_transform(X)
```

## Future Work

In the future, Curve2Vec will support n-dimensional curves and many different embedding algorithms. 
It'll also provide basic utilities needed for working with curves, like curve resampling.


## Contributing
Contributions to Curve2Vec are welcome! If you find a bug or have a feature request, please open an issue on the Github repository. If you would like to contribute code, please fork the repository and submit a pull request