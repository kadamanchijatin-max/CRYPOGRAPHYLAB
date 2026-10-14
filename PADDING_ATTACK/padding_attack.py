import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = AES.block_size

key = os.urandom(BLOCK_SIZE)
iv = os.urandom(BLOCK_SIZE)

plaintext = input("Enter plaintext: ").encode()

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))

queries = 0


def padding_oracle(test_iv, test_ciphertext):
    global queries
    queries += 1

    try:
        cipher = AES.new(key, AES.MODE_CBC, test_iv)
        decrypted = cipher.decrypt(test_ciphertext)
        unpad(decrypted, BLOCK_SIZE)
        return True
    except ValueError:
        return False


def recover_intermediate_block(target_block):
    intermediate = bytearray(BLOCK_SIZE)
    crafted = bytearray(BLOCK_SIZE)

    for padding in range(1, BLOCK_SIZE + 1):
        index = BLOCK_SIZE - padding

        for j in range(index + 1, BLOCK_SIZE):
            crafted[j] = intermediate[j] ^ padding

        found = False

        for guess in range(256):
            crafted[index] = guess

            if not padding_oracle(bytes(crafted), target_block):
                continue

            if padding == 1 and index > 0:
                verification = bytearray(crafted)
                verification[index - 1] ^= 1

                if not padding_oracle(bytes(verification), target_block):
                    continue

            intermediate[index] = guess ^ padding
            found = True
            break

        if not found:
            raise RuntimeError("Unable to recover plaintext block")

    return bytes(intermediate)


def padding_oracle_attack(initial_iv, encrypted):
    if len(initial_iv) != BLOCK_SIZE:
        raise ValueError("Invalid IV length")

    if not encrypted or len(encrypted) % BLOCK_SIZE != 0:
        raise ValueError("Invalid ciphertext length")

    blocks = [
        encrypted[i:i + BLOCK_SIZE]
        for i in range(0, len(encrypted), BLOCK_SIZE)
    ]

    recovered = bytearray()
    previous = initial_iv

    for block in blocks:
        intermediate = recover_intermediate_block(block)

        plaintext_block = bytes(
            intermediate[i] ^ previous[i]
            for i in range(BLOCK_SIZE)
        )

        recovered.extend(plaintext_block)
        previous = block

    return unpad(bytes(recovered), BLOCK_SIZE)


recovered_plaintext = padding_oracle_attack(iv, ciphertext)

print("\nIV:", iv.hex())
print("Ciphertext:", ciphertext.hex())
print("Recovered plaintext:", recovered_plaintext.decode())
print("Total oracle queries:", queries)
print("Recovery successful:", recovered_plaintext == plaintext)
