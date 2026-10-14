# Padding Oracle Attack

## Overview

This assignment demonstrates a Padding Oracle Attack against AES-CBC encryption. It shows how an attacker can recover plaintext without knowing the AES encryption key by exploiting a padding oracle that reveals whether decrypted ciphertext has valid PKCS#7 padding.

## Objectives

- Understand AES-CBC encryption and PKCS#7 padding.
- Implement a padding oracle that checks padding validity.
- Recover plaintext bytes from right to left.
- Count the total number of oracle queries.
- Understand how padding oracle vulnerabilities can be prevented.

## Technologies Used

- Python 3
- PyCryptodome
- AES-CBC encryption
- PKCS#7 padding

## Project Structure

PADDINGATTACK/ ├── paddingattack.py └── README.md


## How It Works

1. A plaintext message is encrypted using AES-CBC with PKCS#7 padding.
2. The padding oracle returns whether the decrypted ciphertext has valid padding.
3. The attack modifies the IV or previous ciphertext block and queries the oracle with different byte values.
4. Valid oracle responses help recover intermediate bytes, which are XORed with the original preceding block to reconstruct the plaintext.
5. The program removes the padding and displays the recovered plaintext and total number of oracle queries.

The attack implementation does not directly access the AES key. The key is used only by the encryption setup and the simulated oracle.

## Installation

Install the required dependency:

python3 -m pip install pycryptodome


## Execution

Run the program:

python3 padding_attack.py


Enter a plaintext when prompted. The program encrypts it, performs the attack, and displays the recovered plaintext, oracle query count, and recovery status.

## Security Recommendations

- Prefer authenticated encryption modes such as AES-GCM.
- Authenticate ciphertext before decrypting when using legacy AES-CBC.
- Avoid exposing distinguishable padding errors or timing differences.
- Use established cryptographic libraries and secure implementations.

## Conclusion

This assignment demonstrates that a padding oracle vulnerability can expose encrypted plaintext without revealing the AES key. It highlights the importance of authenticated encryption and secure error handling.
