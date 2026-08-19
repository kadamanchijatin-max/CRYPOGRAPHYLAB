# main.py

from shift_cipher import encrypt, decrypt
from brute_force_dictionary import brute_force_attack
from chi_square_attack import chi_square_attack


print("===== SHIFT CIPHER CRYPTANALYSIS =====")

plaintext = input("Enter plaintext: ")
key = int(input("Enter key (0-25): "))

ciphertext = encrypt(plaintext, key)

print("\nEncrypted text:", ciphertext)

print("Decrypted text:", decrypt(ciphertext, key))

dictionary_key, dictionary_text, dictionary_score = brute_force_attack(ciphertext)

print("\n--- Dictionary Attack ---")
print("Predicted key:", dictionary_key)
print("Decrypted text:", dictionary_text)
print("Dictionary score:", dictionary_score)

chi_key, chi_text, chi_score = chi_square_attack(ciphertext)

print("\n--- Chi-Square Attack ---")
print("Predicted key:", chi_key)
print("Decrypted text:", chi_text)
print("Chi-Square score:", chi_score)

print("\n--- Comparison ---")
print("Actual key:", key)
print("Dictionary key:", dictionary_key)
print("Chi-Square key:", chi_key)

if dictionary_key == key:
    print("Dictionary attack: Correct")
else:
    print("Dictionary attack: Incorrect")

if chi_key == key:
    print("Chi-Square attack: Correct")
else:
    print("Chi-Square attack: Incorrect")
