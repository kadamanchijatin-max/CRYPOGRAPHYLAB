Cryptographic Random Number Generation Analysis
Overview

This project evaluates operating-system random-number generation mechanisms and investigates their suitability for cryptographic applications.

The experiment compares:

Linux /dev/urandom
OpenSSL rand
Windows Cryptography API: Next Generation (CNG)
Objectives
Generate at least 1 MiB of random data from each source.
Analyze byte-frequency and bit distributions.
Examine repeated patterns and serial correlations.
Apply statistical tests and interpret their results.
Investigate how Linux and Windows manage cryptographically secure random data.
Explain why passing statistical tests does not guarantee cryptographic security.
Technologies
Python 3
Jupyter Notebook
NumPy
SciPy
Pandas
Matplotlib
OpenSSL
Windows CNG API
Project Status

The Linux /dev/urandom and OpenSSL experiments have been conducted. The Windows CNG experiment and final three-way comparison remain to be completed.

Running the Notebook

Install the required Python packages:

bash
python -m pip install -r requirements.txt


Start Jupyter Notebook:

bash
jupyter notebook


Open crypto_randomness_lab.ipynb and run the cells in order.

OpenSSL must be installed for the OpenSSL experiment. The Windows CNG experiment must be executed on Windows.

Statistical Analysis

The notebook examines:

Byte-frequency distributions
Bit-frequency distributions
Repeated bytes and 16-bit words
Serial correlations
Chi-square goodness-of-fit
Monobit frequency
Runs test
Security Considerations

Statistical tests can reveal certain irregularities in random data, but they cannot prove that a generator is cryptographically secure. Cryptographic security also depends on unpredictability, initialization, internal state protection, implementation quality, and resistance to attack.

Disclaimer

This project is for educational and laboratory purposes.
