from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def encrypt_aes_gcm(plaintext, ad, key, nonce):
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    cipher.update(ad)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return ciphertext, tag

def decrypt_aes_gcm(ciphertext, ad, tag, key, nonce):
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    cipher.update(ad)
    ptxt = cipher.decrypt_and_verify(ciphertext, tag)
    return ptxt


msg = b"Testing AES-GCM mode for authenticated ciphers"
associated_data = b"This is a non-secret message!"
key = get_random_bytes(16)
nonce = get_random_bytes(8)
ctxt, tag = encrypt_aes_gcm(msg, associated_data, key, nonce)
print(f"Ciphertext: {ctxt}")
print(f"Tag: {tag}")

ptxt = decrypt_aes_gcm(ctxt, b"rr", tag, key, nonce)
print(f"Plaintext: {ptxt}")
