# Constants for the ASCII values of 'A' and 'Z', representing the upper case letters range.
A = 65  # ASCII value of 'A'
Z = 90  # ASCII value of 'Z'


# Custom modular arithmetic function.
# This function returns the value of x modulo (n2 - n1 + 1), adjusted to the range [n1, n2].
def custom_mod(x, n1, n2):
    return ((x - n1) % (n2 - n1 + 1)) + n1


# Euclidean algorithm to compute the greatest common divisor (gcd) of two numbers.
# It repeatedly applies the formula: a, b = b, a % b until b becomes 0, and then returns a.
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# Extended Euclidean algorithm (egcd) to compute the gcd of a and b, along with coefficients
# x and y such that a * x + b * y = gcd(a, b).
def egcd(a, b):
    # initial values
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1

    # Loop until b becomes 0, updating the coefficients (x0, x1) and (y0, y1) at each step
    while b != 0:
        q = a // b  # Quotient of a divided by b
        r = a % b   # Remainder of a divided by b
        a = b
        b = r
        x = x0 - q * x1  # Update x coefficient
        y = y0 - q * y1  # Update y coefficient
        x0 = x1
        y0 = y1
        x1 = x
        y1 = y

    # Return the gcd along with coefficients x and y
    return (a, x0, y0)


# Check if the provided key is valid for modular arithmetic (multiplicative inverse exists).
# A key is valid if gcd(key, modulus) == 1, meaning the key and modulus are coprime.
def is_valid_key(key, mod):
    if gcd(key, mod) != 1:
        return False
    return True


# Encrypt a plaintext message using the Affine cipher.
# The formula for encryption is: c = (a * p + b) % modulus, where
# 'a' is the multiplier, 'b' is the shift, and modulus is the range of characters.
def affine_encrypt(plaintext, multiplier, shift, modulus):
    # Validate the multiplier key before proceeding with encryption
    if not is_valid_key(multiplier, modulus):
        print("The multiplier value", multiplier, "is not valid")
        exit(1)

    ctxt = ""
    for p in plaintext:
        if (p.isalpha()):
            c = multiplier * ord(p) + shift  # Affine cipher encryption formula
            c = custom_mod(c, A, Z)  # Apply custom modulus to ensure the result is within A-Z range
            ctxt += chr(c)  # Convert the resulting value to a character and append to ciphertext
        else:
            ctxt += p  # Non-alphabet characters remain unchanged

    return ctxt  # Return the encrypted ciphertext


# Decrypt a ciphertext message using the Affine cipher.
# The formula for decryption is: p = (a_inv * (c - b)) % modulus, where
# a_inv is the modular inverse of the multiplier 'a'.
def affine_decrypt(ciphertext, multiplier, shift, modulus):
    # Calculate the modular inverse of the multiplier using the extended Euclidean algorithm
    _, inv, _ = egcd(multiplier, modulus)
    ptxt = ""  # Initialize the plaintext string
    for c in ciphertext:
        # Decrypt only alphabetic characters, ignoring spaces and punctuation
        if (c.isalpha()):
            p = inv * (ord(c) - shift)  # Apply the affine decryption formula
            p = custom_mod(p, A, Z)  # Apply custom modulus to ensure the result is within A-Z range
            ptxt += chr(p)  # Convert the resulting value to a character and append to plaintext
        else:
            ptxt += c  # Non-alphabet characters remain unchanged

    return ptxt  # Return the decrypted plaintext


# Example message to be encrypted and decrypted
msg = "HELLO WORLD!"  # Plaintext message

# Define the affine cipher parameters
a = 5  # Multiplier (must be coprime with the modulus)
shift = 4  # Shift (constant added after multiplying by the multiplier)
modulus = Z - A + 1  # Modulus for uppercase English letters (26 letters)

# Encrypt the message using the affine cipher
ctxt = affine_encrypt(msg, a, shift, modulus)
print("Affine encrypt: ", ctxt)  # Output the encrypted message

# Decrypt the ciphertext back to the original message
ptxt = affine_decrypt(ctxt, a, shift, modulus)
print("Affine decrypt: ", ptxt)  # Output the decrypted message
