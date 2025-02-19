# Constants representing the ASCII values of 'A' and 'Z' for uppercase letters.
# 'A' = 65 and 'Z' = 90, the range of uppercase letters in the ASCII table.
A = 65  # ASCII value for 'A'
Z = 90  # ASCII value for 'Z'


# Custom modular function to ensure that the result stays within the range [n1, n2].
# This function adjusts the value 'x' so that it is wrapped around within the specified range.
# It is used for wrapping letters in the Caesar cipher between 'A' and 'Z'.
def custom_mod(x, n1, n2):
    return ((x - n1) % (n2 - n1 + 1)) + n1

# Caesar cipher decryption function.
# This function takes a text (ciphertext) and a shift value, and returns the decrypted plaintext.
# The Caesar cipher works by shifting the ASCII values of the letters backwards by a certain amount.
def caesar_cipher(text, shift):
    ptxt = ""
    for s in text:
        if (s.isalpha()):  # If the character is a letter (ignoring spaces/punctuation)
            c = ord(s) - shift  # Decrypt the letter by subtracting the shift value
            c = custom_mod(c, A, Z)  # Apply the custom modulus to ensure the result stays within 'A' to 'Z'
            ptxt += chr(c)
        else:
            ptxt += s  # Non-alphabet characters (like spaces and punctuation) remain unchanged
    return ptxt

# The ciphertext to be decoded using different shift values in the Caesar cipher.
ctxt = "WXF HXD LJW LAJLT VN!"

# Try all possible shift values from 1 to 25 (since a shift of 26 would bring us back to the original text)
for shift in range(1, 26):
    print(caesar_cipher(ctxt, shift))  # Print the decrypted text for each shift value
