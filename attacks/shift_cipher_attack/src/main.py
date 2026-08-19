import os

from brute_force_dictionary import dictionary_attack
from chi_square_attack import chi_square_attack


def main():

    print("=" * 60)
    print("       SHIFT CIPHER CRYPTANALYSIS")
    print("=" * 60)

    ciphertext = input("\nEnter ciphertext: ")

    dictionary_path = "../dictionary/english_words.txt"

    # Dictionary Attack
    print("\n" + "-" * 60)
    print("DICTIONARY SCORING ATTACK")
    print("-" * 60)

    dict_key, dict_plaintext, dict_score, dict_results = (
        dictionary_attack(
            ciphertext,
            dictionary_path
        )
    )

    for key, plaintext, score in dict_results:
        print(
            f"Key {key:2d} | "
            f"Score {score:2d} | "
            f"{plaintext}"
        )

    print("\nPredicted Key:", dict_key)
    print("Predicted Plaintext:", dict_plaintext)
    print("Best Dictionary Score:", dict_score)

    # Chi-Square Attack
    print("\n" + "-" * 60)
    print("CHI-SQUARE ATTACK")
    print("-" * 60)

    chi_key, chi_plaintext, chi_score, chi_results = (
        chi_square_attack(ciphertext)
    )

    for key, plaintext, score in chi_results:
        print(
            f"Key {key:2d} | "
            f"Chi-Square {score:.2f} | "
            f"{plaintext}"
        )

    print("\nPredicted Key:", chi_key)
    print("Predicted Plaintext:", chi_plaintext)
    print("Lowest Chi-Square:", chi_score)

    # Comparison
    print("\n" + "=" * 60)
    print("COMPARISON")
    print("=" * 60)

    print("Dictionary Key :", dict_key)
    print("Chi-Square Key :", chi_key)

    if dict_key == chi_key:
        print("Both attacks predicted the same key.")
    else:
        print("The two attacks predicted different keys.")


if __name__ == "__main__":
    main()