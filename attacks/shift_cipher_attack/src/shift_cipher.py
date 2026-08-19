def encrypt(text, key):
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))

        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))

        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))

        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))

        else:
            result += ch

    return result
