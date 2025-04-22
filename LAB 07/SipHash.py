import siphash
from Crypto import Random

# pip install siphash

def sip_hash(key, msg):
    # SipHash 2-4 is the default
    # 2 SipRounds and 4 finalization rounds
    # takes 128-bit key and returns 64 bit tag
    tag = siphash.SipHash_2_4(key, msg)
    return tag.hexdigest()


def bad_verify_SipHash(key, msg, tag):
    digest = sip_hash(key, msg)
    for i in range(len(tag)):
        if tag[i] != digest[i]:
            return False
    return True

def secure_verify_SipHash(key, msg, tag):
    digest = sip_hash(key, msg)
    valid = 0
    for i in range(len(tag)):
        valid |= (tag[i] ^ digest[i])

    return valid==0

msg = b"Testing SipHash"
key = Random.get_random_bytes(16)
tag = sip_hash(key, msg)
print("Message:", msg)
print("Tag:", tag)
print("Verified SipHash:", bad_verify_SipHash(key, msg, tag))
print("Verified SipHash:", secure_verify_SipHash(key, msg, tag))

