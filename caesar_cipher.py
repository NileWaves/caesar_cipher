import string

alphabet = list(string.ascii_lowercase)


def encrypt(pos_change, plaintext):
    plaintext = plaintext.lower()
    plaintext = [*plaintext]  # convert str to list
    ciphertext = []

    for x in plaintext:
        for y in alphabet:
            if x == y:
                position = alphabet.index(y)
                position = position + pos_change
                position = position % 26  # cap the position at 25
                ciphertext.append(alphabet[position])

    ciphertext = "".join(ciphertext)
    return ciphertext


def decrypt(pos_change, ciphertext):
    plaintext = []
    plaintext = encrypt(-pos_change, ciphertext)
    return plaintext
