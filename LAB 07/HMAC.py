import hmac
from Crypto import Random
from Crypto.Hash import SHA256, SHA512


def verify_hmac_sha(key, msg, tag, SHA_version=SHA256):
    mac = hmac.new(key, msg=msg, digestmod=SHA_version).hexdigest()
    return hmac.compare_digest(mac, tag)


key = Random.get_random_bytes(16)
msg = b"Testing HMAC SHA"
print("Message:", msg)

# Using SHA256 as a hash function
tag = hmac.new(key, msg=msg, digestmod=SHA256).hexdigest()
print("HMAC_SHA256 Tag:", tag)
print("Valid tag?:", verify_hmac_sha(key, msg, tag))


# Using SHA512 as a hash function
tag = hmac.new(key, msg=msg, digestmod=SHA512).hexdigest()
print("HMAC_SHA512 Tag:", tag)
print("HMAC SHA valid?:", verify_hmac_sha(key, msg, tag, SHA512))