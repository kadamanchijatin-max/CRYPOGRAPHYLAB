# CRYPOGRAPHYLAB

This repository contains lab work and implementations for cryptography experiments and assignments.

## Project structure

- README.md
- modules/
  - symmetric/            # Symmetric encryption algorithms (AES, DES, etc.)
  - asymmetric/           # Asymmetric algorithms (RSA, ECC)
  - hashing/              # Hash functions and utilities (SHA-256, MD5)
  - signatures/           # Digital signature implementations and demos
  - key_management/       # Key generation, storage, and exchange examples
  - utils/                # Common helpers and utilities used by modules
- docs/                   # Lab reports, documentation, and theory notes
- notebooks/              # Jupyter notebooks used for experiments/demos
- tests/                  # Unit tests for modules
- data/                   # Example inputs, test vectors, and sample files
- scripts/                # Helper scripts to run demos or build artifacts

> Note: If a folder listed above is missing, create it following the names above and place related code inside.

## Modules (brief)

- symmetric: Implementations and examples for block/stream ciphers, modes of operation, and padding schemes.
- asymmetric: Keypair generation, encryption/decryption, and example usage for RSA and ECC.
- hashing: Hash function implementations and collision/resistance demonstrations.
- signatures: Signing and verification examples, including RSA/ECDSA workflows.
- key_management: Key generation, safe storage (simple examples), and key exchange protocols (Diffie-Hellman).
- utils: Helpers for byte/bit conversions, test vector loaders, and common wrappers.

## How to run (example)

1. Install dependencies (create a virtual environment if needed):

   - Python projects: python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

2. Run a module demo (example):

   - python modules/symmetric/demo_aes.py

3. Run tests:

   - pytest

Adjust commands for your environment and language (the repository may contain code in other languages).

## Contribution & Naming

- Add new modules under the `modules/` directory.
- Keep each module self-contained with its own README describing how to run examples.

## Team / Project Info

- Repository: kadamanchijatin-max/CRYPOGRAPHYLAB
- Group: 5
- Members:
  - Jayant Singh — 2024ucp1806
  - Jatin Kadamanchi — 2024ucp1903
- Class: CSE A, Year 4

---

If you want changes (different folder names, more details about each module, or language-specific instructions), tell me what to add and I'll update the README.