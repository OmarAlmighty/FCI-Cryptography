from Crypto.Cipher import AES
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256

# Generate key pairs for Alice
alice_key = ECC.generate(curve="p256")
alice_public_key = alice_key.public_key()
alice_priv_key = alice_key.d

# Generate key pairs for Bob
bob_key = ECC.generate(curve="p256")
bob_public_key = bob_key.public_key()
bob_priv_key = bob_key.d

# Compute the shared secret at Alice's side
alice_secret = alice_priv_key * bob_public_key.pointQ

# Compute the shared secret at Bob's side
bob_secret = bob_priv_key * alice_public_key.pointQ


print(f"alice_secret: {alice_secret.xy}")
print(f"bob_secret: {bob_secret.xy}")
assert alice_secret == bob_secret


# Hash the shared secret to derive a symmetric key
# Use the x-coordinates only
shared_secret_bytes = int(alice_secret.x).to_bytes(32, 'big')  # Convert to bytes
aes_key = SHA256.new(shared_secret_bytes).digest()  # Derive AES key
print(f"aes_key: {aes_key}")

def AES_encrypt(ptxt, key):
    # Create an AES cipher with GCM mode of operation to allow
    # encryption and generating tags
    cipher = AES.new(key, AES.MODE_GCM)
    ctxt, tag = cipher.encrypt_and_digest(ptxt)
    # return the nonce, the ciphertext, and the tag
    return cipher.nonce, ctxt, tag

def AES_decrypt(ctxt, nonce, key, tag):
    # Create an AES cipher with a predefined nonce
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    # Decrypt the message and verify the tag
    ptxt = cipher.decrypt_and_verify(ctxt, tag)
    return ptxt


plaintext = b"This my test message for ECAES"
print(f"plaintext: {plaintext}")
nonce, ctxt, tag = AES_encrypt(plaintext, aes_key)
print(f"nonce: {nonce}")
print(f"ctxt: {ctxt}")
print(f"tag: {tag}")
decrypted = AES_decrypt(ctxt, nonce, aes_key, tag)
print(f"decrypted: {decrypted}")



