# Monoalphabetic Substitution Cipher and Cryptanalysis

## Aim

To implement a Monoalphabetic Substitution Cipher and perform its cryptanalysis using letter-frequency analysis, word-frequency analysis, and word-pattern analysis.

## Objectives

* Implement Monoalphabetic Substitution Cipher.
* Generate ciphertext from plaintext.
* Perform letter-frequency analysis.
* Display ciphertext letters in descending order of frequency.
* Calculate percentage frequency of each letter.
* Identify the most frequent ciphertext letters.
* Perform word-frequency analysis.
* Analyze one-letter, two-letter, and three-letter words.
* Identify repeated words.
* Analyze repeated-letter patterns.
* Iteratively recover plaintext using candidate substitutions.
* Reject incorrect substitution hypotheses.
* Recover the corresponding substitution key.
* Validate the recovered key by re-encrypting the plaintext.

## Input

The plaintext is selected from the assigned page of the book **Modern Cryptography by Katz and Lindell**, according to:

```text
Page Number = Group Number + 30
```

The plaintext is stored in:

```text
plaintext.txt
```

## Output

The program generates:

* Encrypted ciphertext
* Letter-frequency table
* Percentage frequency of letters
* Descending frequency order
* Most frequent ciphertext letters
* Word-frequency information
* One-letter words
* Two-letter words
* Three-letter words
* Repeated words
* Repeated-letter patterns
* Partial plaintext during cryptanalysis
* Current substitution table
* Verification result

The generated ciphertext is stored in:

```text
ciphertext.txt
```

## Functions Implemented

The program contains the following required functions:

```cpp
frequency_analysis()
word_frequency_analysis()
pattern_analysis()
apply_substitution()
display_partial_plaintext()
verify_solution()
```

Additional functions are used for:

```cpp
readFile()
writeFile()
encryptMonoalphabetic()
extractWords()
getPattern()
cryptanalysis()
```

## Cryptanalysis Method

The ciphertext is analyzed without using any cryptographic library.

The following approach is used:

1. Perform letter-frequency analysis.
2. Identify the most frequent ciphertext letters.
3. Analyze one-letter words.
4. Analyze two-letter and three-letter words.
5. Identify repeated words.
6. Identify repeated-letter patterns.
7. Propose candidate substitutions.
8. Apply suspected substitutions to the ciphertext.
9. Examine the resulting partial plaintext.
10. Reject substitutions that produce inconsistent or meaningless text.
11. Continue testing substitutions until meaningful plaintext is recovered.
12. Construct the recovered substitution key.
13. Re-encrypt the recovered plaintext.
14. Compare the generated ciphertext with the original ciphertext.

## Compilation

Compile the program using:

```bash
g++ monoalphabetic.cpp -o mono
```

## Execution

Run the program using:

```bash
./mono
```

## Program Menu

The program provides the following options:

```text
1. Letter Frequency Analysis
2. Word Frequency Analysis
3. Pattern Analysis
4. Add Candidate Substitution
5. Remove Candidate Substitution
6. Display Partial Plaintext
7. Display Current Substitution Table
8. Verify Original Encryption
9. Exit
```

## Verification

The recovered plaintext/key is verified by re-encrypting the plaintext and comparing the resulting ciphertext with the original ciphertext.

If both ciphertexts are identical, the recovered key is considered valid.

## Files

```text
MonoalphabeticCipher/
│
├── monoalphabetic.cpp
├── plaintext.txt
├── ciphertext.txt
└── README.md
```
