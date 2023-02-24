from setuptools import setup, find_packages

setup(
    name='curve2vec',
    version='0.1.0',
    author='Daniel Cieśliński',
    author_email='daniel98c@gmail.com',
    description='A Python package for generating vector embeddings of curves',
    url='https://github.com/danielcieslinski/curve2vec',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='curve embedding representation vector',
    install_requires=[
        'numpy>=1.21.1',
        'scipy>=1.7.1',
        'scikit-learn>=0.24.2',
        'pyefd',
        'matplotlib'
    ],
    python_requires='>=3.7',
)