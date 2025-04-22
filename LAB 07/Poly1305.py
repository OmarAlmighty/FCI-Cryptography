from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
from Crypto import Random


def verify_poly1305(key, msg, tag, nonce):
    mac = Poly1305.new(key=key, cipher=AES, data=msg)
    try:
        mac.hexverify(tag.hexdigest())
        print("Verify: True")
    except ValueError:
        print("The message or the key is wrong")


key = Random.get_random_bytes(32)
msg = b"Testing HMAC SHA"
print("Message:", msg)
tag = Poly1305.new(key=key, cipher=AES, data=msg)

print("Poly1305_AES Tag:", tag.hexdigest())
print("Poly1305_AES Nonce:", tag.nonce.hex())
verify_poly1305(key, msg, tag, tag.nonce)
