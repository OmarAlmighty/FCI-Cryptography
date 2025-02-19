# Constants representing the ASCII values of 'A' and 'Z', which define the range of uppercase letters.
A = 65  # ASCII value for 'A'
Z = 90  # ASCII value for 'Z'

# Custom modulus function to ensure the result stays within the range [n1, n2].
# It adjusts the value 'x' so that it "wraps around" and stays within the given range [n1, n2].
def custom_mod(x, n1, n2):
    return ((x - n1) % (n2 - n1 + 1)) + n1

# Caesar cipher function to encrypt or decrypt a message.
# It shifts each alphabetic character by a specified number of positions (shift).
# Non-alphabetic characters (e.g., spaces or punctuation) are not altered.
def caesar_cipher(text, shift):
    ctxt = ""
    for s in text:
        if (s.isalpha()):  # If the character is an alphabetic letter
            c = ord(s) + shift  # Shift the character by the specified amount (forward or backward)
            c = custom_mod(c, A, Z)  # Ensure the result stays within the range 'A' to 'Z'
            ctxt += chr(c)  # Convert the shifted value back to a character and append it to the ciphertext
        else:
            ctxt += s  # Non-alphabetic characters (like spaces or punctuation) are added unchanged
    return ctxt

# Rot13 is a special case of the Caesar cipher where the shift is always 13.
def rot13_cipher(text):
    ctxt = caesar_cipher(text, 13)
    return ctxt

mytext = "WELCOME TO CLASSICAL CRYPTOGRAPHY!"

# Encrypt the message using the Caesar cipher with a shift of 3.
ctxt1 = caesar_cipher(mytext, 3)
# Encrypt the message using the Rot13 cipher (which uses a shift of 13).
ctxt2 = rot13_cipher(mytext)

print("Caesar cipher (encryption):", ctxt1)
print("Rot13 cipher (encryption):", ctxt2)

ptxt1 = caesar_cipher(ctxt1, -3)  # Decrypt the Caesar cipher by reversing the shift (negative shift)
ptxt2 = rot13_cipher(ctxt2)  # Decrypt the Rot13 cipher (same as encryption since it's symmetric)

print("Caesar cipher (decryption):", ptxt1)  # Print the Caesar cipher decrypted message
print("Rot13 cipher (decryption):", ptxt2)  # Print the Rot13 cipher decrypted message
