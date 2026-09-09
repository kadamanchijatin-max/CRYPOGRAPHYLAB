from vengenere import *


# ============================================================
# CIPHERTEXT
# ============================================================

ciphertext = """
DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA
MKTTF TCCFX
KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH QSVHP
WFKLS LEASE
PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW
NUOVJ MJCLL
OEOFA ZENVM JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQ
ZVRMN WTQSE
OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM
OECBX SESCI
YGUFP KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL
RYELH QSVWB
AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWVvfrom vengenere import *# ============================================================# CIPHERTEXT# ============================================================ciphertext = """DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGAMKTTF TCCFXKFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH QSVHPWFKLS LEASEPWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLWNUOVJ MJCLLOEOFA ZENVM JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQZVRMN WTQSEOTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACMOECBX SESCIYGUFP KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMELRYELH QSVWBAWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWVOVVXH KWQILIEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSETZEDF"""# ============================================================# STEP 1: PREPROCESS# ============================================================ciphertext = clean_ciphertext(ciphertext)print("=" * 70)print("CRYPTANALYSIS OF VIGENERE CIPHER")print("=" * 70)print("\nCleaned ciphertext:")print(ciphertext)print("\nCiphertext length:", len(ciphertext))# ============================================================# STEP 2: KASISKI EXAMINATION# ============================================================candidates, repeated, distances = kasiski_analysis(ciphertext)print("\n" + "=" * 70)print("KASISKI EXAMINATION")print("=" * 70)print("\nRepeated patterns:")for pattern, positions in repeated.items():print(f"{pattern}: {positions}")print("\nDistances between repeated patterns:")for pattern, distance_list in distances.items():print(f"{pattern}: {distance_list}")print("\nCandidate key lengths:")for length, count in candidates:print(f"Key Length = {length:2} "f"Frequency = {count}")# ============================================================# SELECT ESTIMATED KEY LENGTH# ============================================================if not candidates:print("\nNo key length found using Kasiski test.")exit()key_length = candidates[0][0]print("\nEstimated Key Length:",key_length)# ============================================================# BONUS: INDEX OF COINCIDENCE# ============================================================print("\n" + "=" * 70)print("INDEX OF COINCIDENCE")print("=" * 70)groups = split_into_groups(ciphertext,key_length)for i, group in enumerate(groups, start=1):ic = calculate_ic(group)print(f"Group {i}: IC = {ic:.5f}")# ============================================================# STEP 3: SPLIT CIPHERTEXT# ============================================================print("\n" + "=" * 70)print("CIPHERTEXT GROUPS")print("=" * 70)for i, group in enumerate(groups, start=1):print(f"Group {i}: {group}")# ============================================================# STEP 4: FREQUENCY ANALYSIS# ============================================================print("\n" + "=" * 70)print("FREQUENCY ANALYSIS")print("=" * 70)for i, group in enumerate(groups, start=1):frequencies = frequency_analysis(group)print(f"\nGroup {i}")print("-" * 50)for letter, count in frequencies.items():print(f"{letter}: {count:2}",end=" ")if ((ord(letter) - ord('A') + 1)% 6 == 0):print()# ============================================================# STEP 5: RECOVER KEY# ============================================================key, shift_details = find_key(groups)print("\n" + "=" * 70)print("KEY RECOVERY")print("=" * 70)for i, (shift, score) in enumerate(shift_details,start=1):key_letter = chr(ord('A') + shift)print(f"Group {i}: "f"Shift = {shift:2} | "f"Key Letter = {key_letter} | "f"Chi-Square = {score:.2f}")print("\nRecovered Key:", key)# ============================================================# STEP 6: DECRYPT# ============================================================plaintext = vigenere_decrypt(ciphertext,key)print("\n" + "=" * 70)print("RECOVERED PLAINTEXT")print("=" * 70)print(plaintext)# ============================================================# STEP 7: RE-ENCRYPT# ============================================================re_encrypted = vigenere_encrypt(plaintext,key)print("\n" + "=" * 70)print("RE-ENCRYPTED CIPHERTEXT")print("=" * 70)print(re_encrypted)# ============================================================# STEP 8: VERIFY# ============================================================verification = verify(ciphertext,plaintext,key)print("\n" + "=" * 70)print("VERIFICATION")print("=" * 70)if verification:print("SUCCESS: Re-encryption matches ""the original ciphertext.")else:print("FAILED: Re-encryption does not ""match the original ciphertext.")her means

# ============================================================
# STEP 1: PREPROCESS
# ============================================================

ciphertext = clean_ciphertext(ciphertext)

print("=" * 70)
print("CRYPTANALYSIS OF VIGENERE CIPHER")
print("=" * 70)

print("\nCleaned ciphertext:")
print(ciphertext)

print("\nCiphertext length:", len(ciphertext))


# ============================================================
# STEP 2: KASISKI EXAMINATION
# ============================================================

candidates, repeated, distances = kasiski_analysis(
    ciphertext
)

print("\n" + "=" * 70)
print("KASISKI EXAMINATION")
print("=" * 70)


print("\nRepeated patterns:")

for pattern, positions in repeated.items():

    print(
        f"{pattern}: {positions}"
    )


print("\nDistances between repeated patterns:")

for pattern, distance_list in distances.items():

    print(
        f"{pattern}: {distance_list}"
    )


print("\nCandidate key lengths:")

for length, count in candidates:

    print(
        f"Key Length = {length:2} "
        f"Frequency = {count}"
    )


# ============================================================
# SELECT ESTIMATED KEY LENGTH
# ============================================================

if not candidates:

    print("\nNo key length found using Kasiski test.")
    exit()


key_length = candidates[0][0]

print(
    "\nEstimated Key Length:",
    key_length
)


# ============================================================
# BONUS: INDEX OF COINCIDENCE
# ============================================================

print("\n" + "=" * 70)
print("INDEX OF COINCIDENCE")
print("=" * 70)

groups = split_into_groups(
    ciphertext,
    key_length
)

for i, group in enumerate(groups, start=1):

    ic = calculate_ic(group)

    print(
        f"Group {i}: IC = {ic:.5f}"
    )


# ============================================================
# STEP 3: SPLIT CIPHERTEXT
# ============================================================

print("\n" + "=" * 70)
print("CIPHERTEXT GROUPS")
print("=" * 70)

for i, group in enumerate(groups, start=1):

    print(
        f"Group {i}: {group}"
    )


# ============================================================
# STEP 4: FREQUENCY ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("FREQUENCY ANALYSIS")
print("=" * 70)

for i, group in enumerate(groups, start=1):

    frequencies = frequency_analysis(group)

    print(f"\nGroup {i}")
    print("-" * 50)

    for letter, count in frequencies.items():

        print(
            f"{letter}: {count:2}",
            end="    "
        )

        if (
            (ord(letter) - ord('A') + 1)
            % 6 == 0
        ):
            print()


# ============================================================
# STEP 5: RECOVER KEY
# ============================================================

key, shift_details = find_key(groups)

print("\n" + "=" * 70)
print("KEY RECOVERY")
print("=" * 70)

for i, (shift, score) in enumerate(
    shift_details,
    start=1
):

    key_letter = chr(
        ord('A') + shift
    )

    print(
        f"Group {i}: "
        f"Shift = {shift:2} | "
        f"Key Letter = {key_letter} | "
        f"Chi-Square = {score:.2f}"
    )


print("\nRecovered Key:", key)


# ============================================================
# STEP 6: DECRYPT
# ============================================================

plaintext = vigenere_decrypt(
    ciphertext,
    key
)

print("\n" + "=" * 70)
print("RECOVERED PLAINTEXT")
print("=" * 70)

print(plaintext)


# ============================================================
# STEP 7: RE-ENCRYPT
# ============================================================

re_encrypted = vigenere_encrypt(
    plaintext,
    key
)

print("\n" + "=" * 70)
print("RE-ENCRYPTED CIPHERTEXT")
print("=" * 70)

print(re_encrypted)


# ============================================================
# STEP 8: VERIFY
# ============================================================

verification = verify(
    ciphertext,
    plaintext,
    key
)

print("\n" + "=" * 70)
print("VERIFICATION")
print("=" * 70)

if verification:

    print(
        "SUCCESS: Re-encryption matches "
        "the original ciphertext."
    )

else:

    print(
        "FAILED: Re-encryption does not "
        "match the original ciphertext."
    )