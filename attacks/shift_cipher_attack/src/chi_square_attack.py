from collections import Counter

from shift_cipher import decrypt


ENGLISH_FREQUENCIES = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074
}


def chi_square_score(text):

    letters = [
        char.lower()
        for char in text
        if char.isalpha()
    ]

    total_letters = len(letters)

    if total_letters == 0:
        return float("inf")

    counts = Counter(letters)

    chi_square = 0

    for letter in ENGLISH_FREQUENCIES:

        observed = counts.get(letter, 0)

        expected = (
            ENGLISH_FREQUENCIES[letter] * total_letters
        )

        chi_square += (
            (observed - expected) ** 2
        ) / expected

    return chi_square


def chi_square_attack(ciphertext):

    best_key = None
    best_plaintext = None
    best_score = float("inf")

    results = []

    for key in range(26):

        plaintext = decrypt(ciphertext, key)

        score = chi_square_score(plaintext)

        results.append((key, plaintext, score))

        if score < best_score:

            best_score = score
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext, best_score, results


if __name__ == "__main__":

    ciphertext = input("Enter ciphertext: ")

    key, plaintext, score, results = chi_square_attack(
        ciphertext
    )

    print("\nChi-Square Attack Results")
    print("-------------------------")

    for k, text, s in results:
        print(
            f"Key {k:2d}: "
            f"Chi-Square = {s:.2f} : {text}"
        )

    print("\nPredicted Key:", key)
    print("Predicted Plaintext:", plaintext)
    print("Chi-Square Score:", score)