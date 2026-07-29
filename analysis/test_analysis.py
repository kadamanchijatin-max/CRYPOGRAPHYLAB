from collections import Counter

file_path = "datasets/sample.txt"

with open(file_path, "r") as file:
    text = file.read()

print("Characters:", len(text))
print("Words:", len(text.split()))
print("Lines:", len(text.splitlines()))
print("Unique Characters:", len(set(text)))

letters = [ch.lower() for ch in text if ch.isalpha()]
frequency = Counter(letters)

print("\nLetter Frequency:")
for letter in sorted(frequency):
    print(f"{letter}: {frequency[letter]}")
