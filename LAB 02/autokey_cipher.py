def autokey_encrypt(plaintext, key):
    ciphertext = []
    key_index = 0  # To track position in key

    # Process each character in plaintext
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():  # Only encrypt letters
            k = ord(key[key_index]) - ord('A')  # Get shift value from the key
            cipher_char = chr((ord(plaintext[i]) - ord('A') + k) % 26 + ord('A'))
            ciphertext.append(cipher_char)

            # Extend key by appending the encrypted letter from the plaintext
            key += plaintext[i]  # Add the current plaintext character to the key
            key_index += 1
        else:
            ciphertext.append(plaintext[i])  # Non-alphabetic characters remain unchanged

    return ''.join(ciphertext)


def autokey_decrypt(ciphertext, key):
    plaintext = []
    key_index = 0  # To track position in key

    # Process each character in ciphertext
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():  # Only decrypt letters
            k = ord(key[key_index]) - ord('A')  # Get shift value from the key
            plain_char = chr((ord(ciphertext[i]) - ord('A') - k) % 26 + ord('A'))
            plaintext.append(plain_char)

            # Add the decrypted letter to the key
            key += plain_char  # Append the decrypted letter to the key
            key_index += 1
        else:
            plaintext.append(ciphertext[i])  # Non-alphabetic characters remain unchanged

    return ''.join(plaintext)


key = "AUTOKEY"
plaintext = "THIS TEXT WAS ENCRYPTED WITH AN AUTOKEY CIPHER"

ctxt = autokey_encrypt(plaintext, key)
print(ctxt)

ptxt = autokey_decrypt(ctxt, key)
print(ptxt)
