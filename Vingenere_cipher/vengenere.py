from collections import Counter


# ------------------------------------------------------------
# 1. CLEAN CIPHERTEXT
# ------------------------------------------------------------

def clean_ciphertext(ciphertext):
    """Remove spaces/special characters and convert to uppercase."""
    return ''.join(
        ch for ch in ciphertext.upper()
        if ch.isalpha()
    )


# ------------------------------------------------------------
# 2. FIND REPEATED PATTERNS
# ------------------------------------------------------------

def find_repeated_patterns(ciphertext, min_length=3, max_length=5):
    """Find repeated sequences of length 3 to 5."""

    patterns = {}

    for length in range(min_length, max_length + 1):

        for i in range(len(ciphertext) - length + 1):

            pattern = ciphertext[i:i + length]

            if pattern not in patterns:
                patterns[pattern] = []

            patterns[pattern].append(i)

    # Keep only patterns which occur more than once
    repeated = {
        pattern: positions
        for pattern, positions in patterns.items()
        if len(positions) > 1
    }

    return repeated


# ------------------------------------------------------------
# 3. CALCULATE DISTANCES
# ------------------------------------------------------------

def calculate_distances(repeated_patterns):
    """Find distances between repeated occurrences."""

    distances = {}

    for pattern, positions in repeated_patterns.items():

        if len(positions) > 1:

            distances[pattern] = []

            for i in range(len(positions) - 1):

                distance = (
                    positions[i + 1]
                    - positions[i]
                )

                distances[pattern].append(distance)

    return distances


# ------------------------------------------------------------
# 4. FIND FACTORS
# ------------------------------------------------------------

def find_factors(number, max_factor=30):
    """Find factors of a distance."""

    factors = []

    for i in range(2, min(number, max_factor) + 1):

        if number % i == 0:
            factors.append(i)

    return factors


# ------------------------------------------------------------
# 5. KASISKI ANALYSIS
# ------------------------------------------------------------

def kasiski_analysis(ciphertext):
    """
    Perform Kasiski examination.

    Repeated patterns -> distances -> factors
    -> candidate key lengths.
    """

    repeated = find_repeated_patterns(ciphertext)

    distances = calculate_distances(repeated)

    factor_count = Counter()

    for pattern, distance_list in distances.items():

        for distance in distance_list:

            factors = find_factors(distance)

            for factor in factors:
                factor_count[factor] += 1

    candidates = factor_count.most_common()

    return candidates, repeated, distances


# ------------------------------------------------------------
# 6. INDEX OF COINCIDENCE
# ------------------------------------------------------------

def calculate_ic(text):
    """Calculate Index of Coincidence."""

    n = len(text)

    if n <= 1:
        return 0

    counts = Counter(text)

    numerator = sum(
        count * (count - 1)
        for count in counts.values()
    )

    return numerator / (n * (n - 1))


# ------------------------------------------------------------
# 7. SPLIT INTO GROUPS
# ------------------------------------------------------------

def split_into_groups(ciphertext, key_length):
    """
    Divide ciphertext into groups according to key length.
    """

    groups = []

    for i in range(key_length):

        groups.append(
            ciphertext[i::key_length]
        )

    return groups


# ------------------------------------------------------------
# 8. FREQUENCY ANALYSIS
# ------------------------------------------------------------

def frequency_analysis(group):
    """Calculate A-Z frequency for a group."""

    counts = Counter(group)

    frequency = {}

    for i in range(26):

        letter = chr(ord('A') + i)

        frequency[letter] = counts.get(
            letter,
            0
        )

    return frequency


# ------------------------------------------------------------
# 9. FIND SHIFT
# ------------------------------------------------------------

def find_shift(group):
    """
    Find the most probable Caesar shift
    using chi-square analysis.
    """

    english_freq = {
        'A': 0.08167,
        'B': 0.01492,
        'C': 0.02782,
        'D': 0.04253,
        'E': 0.12702,
        'F': 0.02228,
        'G': 0.02015,
        'H': 0.06094,
        'I': 0.06966,
        'J': 0.00153,
        'K': 0.00772,
        'L': 0.04025,
        'M': 0.02406,
        'N': 0.06749,
        'O': 0.07507,
        'P': 0.01929,
        'Q': 0.00095,
        'R': 0.05987,
        'S': 0.06327,
        'T': 0.09056,
        'U': 0.02758,
        'V': 0.00978,
        'W': 0.02360,
        'X': 0.00150,
        'Y': 0.01974,
        'Z': 0.00074
    }

    n = len(group)

    best_shift = 0
    best_score = float('inf')

    # Try every possible Caesar shift
    for shift in range(26):

        decrypted = []

        for ch in group:

            value = (
                ord(ch)
                - ord('A')
                - shift
            ) % 26

            decrypted.append(
                chr(value + ord('A'))
            )

        counts = Counter(decrypted)

        chi_square = 0

        for letter in english_freq:

            observed = counts.get(
                letter,
                0
            )

            expected = (
                english_freq[letter] * n
            )

            if expected > 0:

                chi_square += (
                    (observed - expected) ** 2
                ) / expected

        if chi_square < best_score:

            best_score = chi_square
            best_shift = shift

    return best_shift, best_score


# ------------------------------------------------------------
# 10. FIND KEY
# ------------------------------------------------------------

def find_key(groups):
    """Combine shifts to obtain probable Vigenere key."""

    key = ""
    shift_details = []

    for group in groups:

        shift, score = find_shift(group)

        key += chr(
            ord('A') + shift
        )

        shift_details.append(
            (shift, score)
        )

    return key, shift_details


# ------------------------------------------------------------
# 11. VIGENERE DECRYPT
# ------------------------------------------------------------

def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using recovered key."""

    plaintext = []

    for i, ch in enumerate(ciphertext):

        cipher_value = (
            ord(ch) - ord('A')
        )

        key_value = (
            ord(key[i % len(key)])
            - ord('A')
        )

        plain_value = (
            cipher_value - key_value
        ) % 26

        plaintext.append(
            chr(plain_value + ord('A'))
        )

    return ''.join(plaintext)


# ------------------------------------------------------------
# 12. VIGENERE ENCRYPT
# ------------------------------------------------------------

def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using Vigenere key."""

    ciphertext = []

    for i, ch in enumerate(plaintext):

        plain_value = (
            ord(ch) - ord('A')
        )

        key_value = (
            ord(key[i % len(key)])
            - ord('A')
        )

        cipher_value = (
            plain_value + key_value
        ) % 26

        ciphertext.append(
            chr(cipher_value + ord('A'))
        )

    return ''.join(ciphertext)


# ------------------------------------------------------------
# 13. VERIFY
# ------------------------------------------------------------

def verify(original_ciphertext, plaintext, key):
    """
    Re-encrypt plaintext and check whether it matches
    the original ciphertext.
    """

    re_encrypted = vigenere_encrypt(
        plaintext,
        key
    )

    return re_encrypted == original_ciphertext
