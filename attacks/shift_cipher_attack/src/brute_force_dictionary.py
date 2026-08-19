from shift_cipher import decrypt
import re
import os


def load_dictionary():
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "dictionary",
        "english_words.txt"
    )

    with open(path, "r") as file:
        words = set(word.strip().lower() for word in file)

    return words


def dictionary_score(text, dictionary):
    words = re.findall(r"[a-zA-Z]+", text.lower())

    score = 0

    for word in words:
        if word in dictionary:
            score += 1

    return score


def brute_force_attack(ciphertext):
    dictionary = load_dictionary()

    best_key = 0
    best_text = ""
    best_score = -1

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = dictionary_score(plaintext, dictionary)

        if score > best_score:
            best_score = score
            best_key = key
            best_text = plaintext

    return best_key, best_text, best_score
