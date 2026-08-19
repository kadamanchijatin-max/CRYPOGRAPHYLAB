import os
import re

from shift_cipher import decrypt


def load_dictionary(dictionary_path):
    words = set()

    with open(dictionary_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()

            if word:
                words.add(word)

    return words


def dictionary_score(text, dictionary):
    words = re.findall(r"[a-zA-Z]+", text.lower())

    score = 0

    for word in words:
        if word in dictionary:
            score += 1

    return score


def dictionary_attack(ciphertext, dictionary_path):
    dictionary = load_dictionary(dictionary_path)

    best_key = None
    best_plaintext = None
    best_score = -1

    results = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)

        score = dictionary_score(plaintext, dictionary)

        results.append((key, plaintext, score))

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext, best_score, results


if __name__ == "__main__":

    ciphertext = input("Enter ciphertext: ")

    dictionary_path = "dictionary/english_words.txt"

    key, plaintext, score, results = dictionary_attack(
        ciphertext,
        dictionary_path
    )

    print("\nDictionary Attack Results")
    print("-------------------------")

    for k, text, s in results:
        print(f"Key {k:2d}: Score = {s:2d} : {text}")

    print("\nPredicted Key:", key)
    print("Predicted Plaintext:", plaintext)
    print("Dictionary Score:", score)