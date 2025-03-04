from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes


# Function to encrypt plaintext with ChaCha20
def chacha20_encrypt(key, nonce, plaintext):
    cipher = ChaCha20.new(key=key, nonce=nonce)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


# Function to decrypt ciphertext with ChaCha20
def chacha20_decrypt(key, nonce, ciphertext):
    cipher = ChaCha20.new(key=key, nonce=nonce)

    # Decrypt the ciphertext
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text


# 256-bit key (32 bytes)
key = get_random_bytes(32)

# 64-bit nonce (8 bytes)
nonce = get_random_bytes(8)

plaintext = b"Hello, ChaCha20 encryption and decryption!"

print("Plaintext:", plaintext)

# Encrypt the plaintext
ciphertext = chacha20_encrypt(key, nonce, plaintext)
print("Ciphertext:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_text = chacha20_decrypt(key, nonce, ciphertext)
print("Decrypted text:", decrypted_text)
