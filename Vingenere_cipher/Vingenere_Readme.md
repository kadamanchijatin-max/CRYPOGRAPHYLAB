# Vigenère Cipher Cryptanalysis

## Overview

This assignment implements **Vigenère Cipher cryptanalysis** to recover the unknown encryption key and decrypt a given ciphertext.

The program uses classical cryptanalysis techniques such as:

* Kasiski Examination
* Index of Coincidence
* Frequency Analysis
* Chi-Square Analysis

After recovering the key, the program performs **Vigenère decryption** to obtain the plaintext. It then **re-encrypts the plaintext using the recovered key** and verifies that the generated ciphertext matches the original ciphertext.

---

## Objectives

The main objectives of this assignment are:

1. Understand the Vigenère Cipher.
2. Implement Vigenère encryption and decryption.
3. Determine the probable key length using Kasiski Examination.
4. Use Index of Coincidence to analyze ciphertext groups.
5. Perform frequency analysis on each group.
6. Recover the key using Chi-Square analysis.
7. Decrypt the ciphertext using the recovered key.
8. Re-encrypt the plaintext to verify the result.

---

## Vigenère Cipher

The Vigenère Cipher is a polyalphabetic substitution cipher based on a repeating keyword.

The alphabet is represented using numbers:

```text
A = 0
B = 1
C = 2
...
Z = 25
```

### Encryption

The plaintext and key values are added modulo 26:

```text
Cᵢ = (Pᵢ + Kᵢ) mod 26
```

Where:

* `Pᵢ` = plaintext value
* `Kᵢ` = key value
* `Cᵢ` = ciphertext value

### Decryption

The key is subtracted from the ciphertext modulo 26:

```text
Pᵢ = (Cᵢ - Kᵢ) mod 26
```

The modulo operation ensures that the result remains within the range `0–25`.

---

## Cryptanalysis Approach

In this assignment, the key is **not directly provided**. Therefore, the program attempts to recover the key from the ciphertext.

The complete process is:

```text
Ciphertext
    |
    v
Preprocessing
    |
    v
Kasiski Examination
    |
    v
Estimate Key Length
    |
    v
Index of Coincidence
    |
    v
Split Ciphertext into Groups
    |
    v
Frequency Analysis
    |
    v
Chi-Square Analysis
    |
    v
Recover Key
    |
    v
Vigenère Decryption
    |
    v
Plaintext
    |
    v
Re-encryption
    |
    v
Verification
```

---

## 1. Preprocessing

The ciphertext initially contains spaces and newlines.

The `clean_ciphertext()` function removes unnecessary characters and keeps only alphabetic characters.

Example:

```text
DAZFI SFSPA VQLSN
```

becomes:

```text
DAZFISFSPAVQLSN
```

This makes positional and frequency analysis easier.

---

## 2. Kasiski Examination

Kasiski Examination is used to estimate the **length of the unknown Vigenère key**.

The method searches for repeated sequences in the ciphertext.

For example:

```text
ABC ............... ABC
```

If the repeated sequences occur at different positions, the distance between their positions is calculated.

The factors of these distances provide possible key lengths.

The program displays:

```text
Repeated patterns
Distances between repeated patterns
Candidate key lengths
```

The most likely key length is selected for further analysis.

---

## 3. Index of Coincidence

After estimating the key length, the ciphertext is divided into groups.

For example, if the key length is `3`:

```text
Group 1 → positions 0, 3, 6, 9, ...
Group 2 → positions 1, 4, 7, 10, ...
Group 3 → positions 2, 5, 8, 11, ...
```

Each group is encrypted using the same key character.

The Index of Coincidence (IC) is calculated for each group to determine how closely its letter distribution resembles natural language.

---

## 4. Frequency Analysis

Each ciphertext group is analyzed separately.

The frequency of every alphabetic character is calculated.

Example:

```text
A: 3
B: 1
C: 8
D: 2
E: 12
...
```

English has a characteristic letter frequency distribution, with letters such as `E`, `T`, `A`, and `O` occurring relatively frequently.

This property helps determine the Caesar shift corresponding to each key character.

---

## 5. Chi-Square Analysis

For every ciphertext group, all 26 possible Caesar shifts are tested.

The resulting letter distribution is compared with the expected English letter frequency distribution using the Chi-Square statistic.

The shift producing the **lowest Chi-Square value** is selected as the most likely shift.

The shift is then converted into a key character:

```text
0  → A
1  → B
2  → C
...
25 → Z
```

For example:

```text
Group 1 → Shift 3  → D
Group 2 → Shift 14 → O
Group 3 → Shift 6  → G
```

Therefore:

```text
Recovered Key = DOG
```

---

## 6. Vigenère Decryption

Once the key is recovered, the ciphertext is decrypted using:

```text
Pᵢ = (Cᵢ - Kᵢ) mod 26
```

In the program:

```python
plaintext = vigenere_decrypt(ciphertext, key)
```

This produces the recovered plaintext.

---

## 7. Vigenère Re-encryption

To verify that the recovered key and plaintext are correct, the plaintext is encrypted again using the recovered key.

```python
re_encrypted = vigenere_encrypt(plaintext, key)
```

The encryption formula is:

```text
Cᵢ = (Pᵢ + Kᵢ) mod 26
```

The resulting ciphertext should match the original ciphertext.

---

## 8. Verification

The final step compares the re-encrypted ciphertext with the original ciphertext.

```python
verification = verify(
    ciphertext,
    plaintext,
    key
)
```

If both ciphertexts match:

```text
SUCCESS: Re-encryption matches the original ciphertext.
```

Otherwise:

```text
FAILED: Re-encryption does not match the original ciphertext.
```

This provides a final consistency check for the recovered key and plaintext.

---

## Project Structure

A typical project structure is:

```text
Vigenere-Cryptanalysis/
│
├── vengenere.py
├── main.py
└── README.md
```

### `vengenere.py`

Contains the implementation of the Vigenère cipher and cryptanalysis functions.

It includes functions such as:

```text
clean_ciphertext()
kasiski_analysis()
split_into_groups()
calculate_ic()
frequency_analysis()
find_key()
vigenere_encrypt()
vigenere_decrypt()
verify()
```

### `main.py`

Contains the ciphertext and executes the complete cryptanalysis pipeline.

### `README.md`

Contains documentation explaining the assignment, methodology, algorithms, and execution process.

---

## How to Run

Make sure Python 3 is installed.

Clone or download the project and navigate to the project directory.

Run:

```bash
python main.py
```

The program will display:

1. Cleaned ciphertext
2. Ciphertext length
3. Repeated patterns
4. Distances between repeated patterns
5. Candidate key lengths
6. Index of Coincidence
7. Ciphertext groups
8. Frequency analysis
9. Recovered key
10. Recovered plaintext
11. Re-encrypted ciphertext
12. Verification result

---

## Important Concepts

### Vigenère Encryption

```text
Plaintext + Key
      ↓
   Modulo 26
      ↓
 Ciphertext
```

### Vigenère Decryption

```text
Ciphertext - Key
      ↓
   Modulo 26
      ↓
  Plaintext
```

### Cryptanalysis

```text
Ciphertext
     ↓
Kasiski Examination
     ↓
Key Length
     ↓
Frequency Analysis
     ↓
Chi-Square
     ↓
Key Recovery
     ↓
Decryption
```

---

## Key Insight

The main idea behind breaking a Vigenère Cipher is:

> Once the key length is known, the ciphertext can be divided into separate groups, where each group behaves approximately like a Caesar cipher.

Therefore, the problem changes from breaking one Vigenère cipher into solving several smaller Caesar-cipher problems using statistical analysis.

---

## Conclusion

This assignment demonstrates both the operation and cryptanalysis of the Vigenère Cipher.

The program:

* Implements Vigenère encryption.
* Implements Vigenère decryption.
* Estimates the unknown key length using Kasiski Examination.
* Uses Index of Coincidence for statistical analysis.
* Uses frequency analysis to study ciphertext groups.
* Uses Chi-Square analysis to recover key characters.
* Decrypts the ciphertext using the recovered key.
* Re-encrypts the plaintext for verification.

Thus, the assignment demonstrates how a classical polyalphabetic cipher can be analyzed and broken using statistical cryptanalysis techniques.
