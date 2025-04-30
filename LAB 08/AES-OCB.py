from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_aes_ocb(plaintext, ad, key, nonce):
    cipher = AES.new(key, AES.MODE_OCB, nonce=nonce)
    cipher.update(ad)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return ciphertext, tag


def decrypt_aes_ocb(ciphertext, ad, tag, key, nonce):
    cipher = AES.new(key, AES.MODE_OCB, nonce=nonce)
    cipher.update(ad)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext


msg = b"Testing AES-OCB mode for authenticated ciphers"
associated_data = b"This is a non-secret message!"
key = get_random_bytes(16)
nonce = get_random_bytes(8)
ctxt, tag = encrypt_aes_ocb(msg, associated_data, key, nonce)
print(f"Ciphertext: {ctxt}")
print(f"Tag: {tag}")

ptxt = decrypt_aes_ocb(ctxt, associated_data, tag, key, nonce)
print(f"Plaintext: {ptxt}")
