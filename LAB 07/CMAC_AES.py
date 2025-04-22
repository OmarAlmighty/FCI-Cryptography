from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import CMAC


def cmac_aes_128(key, msg):
    mac = CMAC.new(key, ciphermod=AES, msg=msg)
    return mac.hexdigest()


def cmac_aes_128_verify(key, msg, tag):
    mac = CMAC.new(key, ciphermod=AES, msg=msg)
    # hexverify() will throw an exception if invalid.
    try:
        mac.hexverify(tag)
        return True
    except ValueError:
        print("CMAC is invalid!")
        return False


msg = b"Testing CMAC AES"
key = Random.get_random_bytes(16)
print("Message:", msg)

tag = cmac_aes_128(key, msg)
print("Tag:", tag)
print("Valid tag?", cmac_aes_128_verify(key, msg, tag))
