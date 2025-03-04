from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes


# Function to encrypt plaintext with Salsa20
def salsa20_encrypt(key, nonce, plaintext):
    # Create a Salsa20 cipher instance
    cipher = Salsa20.new(key=key, nonce=nonce)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


# Function to decrypt ciphertext with Salsa20
def salsa20_decrypt(key, nonce, ciphertext):
    # Create a Salsa20 cipher instance
    cipher = Salsa20.new(key=key, nonce=nonce)

    # Decrypt the ciphertext
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text


# 256-bit key for Salsa20 (32 bytes)
key = get_random_bytes(32)

# 64-bit nonce for Salsa20 (8 bytes)
nonce = get_random_bytes(8)

plaintext = b"Hello, Salsa20 encryption and decryption!"

print("Plaintext:", plaintext)

# Encrypt the plaintext
ciphertext = salsa20_encrypt(key, nonce, plaintext)
print("Ciphertext:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_text = salsa20_decrypt(key, nonce, ciphertext)
print("Decrypted text:", decrypted_text)
