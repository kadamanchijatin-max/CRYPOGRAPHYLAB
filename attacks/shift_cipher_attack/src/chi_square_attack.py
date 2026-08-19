# chi_square_attack.py

from shift_cipher import decrypt


# Expected English letter frequencies
english_frequency = [
    8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02,
    6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75,
    7.51, 1.93, 0.10, 5.99, 6.33, 9.06, 2.76,
    0.10, 2.36, 0.15, 1.97, 0.07
]


def chi_square_score(text):
    text = text.lower()

    counts = [0] * 26
    total = 0

    for ch in text:
        if 'a' <= ch <= 'z':
            counts[ord(ch) - ord('a')] += 1
            total += 1

    if total == 0:
        return float('inf')

    score = 0

    for i in range(26):
        expected = total * english_frequency[i] / 100

        if expected > 0:
            score += (counts[i] - expected) ** 2 / expected

    return score


def chi_square_attack(ciphertext):
    best_key = 0
    best_text = ""
    best_score = float('inf')

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = chi_square_score(plaintext)

        if score < best_score:
            best_score = score
            best_key = key
            best_text = plaintext

    return best_key, best_text, best_score
