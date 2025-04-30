from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Hash import CMAC


def EaM(data, key, nonce):
    aes = AES.new(key, AES.MODE_CTR, nonce=nonce)
    cmac = CMAC.new(key, ciphermod=AES)
    ctxt = aes.encrypt(data)
    mac = cmac.update(data).hexdigest()
    return ctxt, mac


def EaM_decrypt(ctxt, tag, key, nonce):
    aes = AES.new(key, AES.MODE_CTR, nonce=nonce)
    ptxt = aes.decrypt(ctxt)
    cmac = CMAC.new(key, ciphermod=AES, msg=ptxt)
    try:
        cmac.hexverify(tag)
        return ptxt
    except:
        print("Invalid tag in EaM_decrypt")


# ---------------------------------------------------------        
def EtM(data, key, nonce):
    aes = AES.new(key, AES.MODE_CTR, nonce=nonce)
    cmac = CMAC.new(key, ciphermod=AES)
    ctxt = aes.encrypt(data)
    mac = cmac.update(ctxt).hexdigest()
    return ctxt, mac


def EtM_decrypt(ctxt, tag, key, nonce):
    aes = AES.new(key, AES.MODE_CTR, nonce=nonce)
    cmac = CMAC.new(key, ciphermod=AES, msg=ctxt)
    try:
        cmac.hexverify(tag)
        ptxt = aes.decrypt(ctxt)
        return ptxt
    except:
        print("Invalid tag in EtM_decrypt")


# ---------------------------------------------------------

def MtE(data, key, nonce):
    aes = AES.new(key, AES.MODE_CTR, nonce=nonce)
    cmac = CMAC.new(key, ciphermod=AES)
    mac = cmac.update(data).digest()
    ctxt = aes.encrypt(data + mac)
    return ctxt


def MtE_decrypt(ctxt, key, nonce):
    # Decrypt the ciphertext
    aes = AES.new(key, AES.MODE_CTR, nonce=nonce)
    ptxt_tag = aes.decrypt(ctxt)
    # Split plaintext and tag (assuming 16-byte tag)
    tag_size = 16
    if len(ptxt_tag) < tag_size:
        raise ValueError("Ciphertext too short to contain a valid tag")
    ptxt = ptxt_tag[:-tag_size]
    tag = ptxt_tag[-tag_size:]
    cmac = CMAC.new(key, ciphermod=AES, msg=ptxt)
    try:
        cmac.verify(tag)
        return ptxt
    except ValueError:
        raise ValueError("Invalid tag in MtE_decrypt")


key = get_random_bytes(16)
data = b'Testing different authenticated encryption methods'
print(f"Key: {key}")
print(f"Data: {data}")
##########################################################
print("=====Encrypt and MAC (Encrypt)=====")
n1 = get_random_bytes(8)
c1, t1 = EaM(data, key, n1)
print(f"ciphertext: {c1}")
print(f"tag: {t1}")
print("=====Encrypt and MAC (Decrypt)=====")
p1 = EaM_decrypt(c1, t1, key, n1)
print(f"Decrypt: {p1}")
##########################################################
print("\n\n=====Encrypt then MAC (Encrypt)=====")
n2 = get_random_bytes(8)
c2, t2 = EtM(data, key, n2)
print(f"Ciphertext: {c2}")
print(f"tag: {t2}")
print("=====Decrypt then MAC (Decrypt)=====")
p2 = EtM_decrypt(c2, t2, key, n2)
print(f"Decrypt: {p2}")
##########################################################
print("\n\n=====Encrypt then MAC (Encrypt)=====")
n3 = get_random_bytes(8)
c3 = MtE(data, key, n3)
print(f"Ciphertext: {c3}")
print("=====MAC then Encrypt (Decrypt)=====")
p3 = MtE_decrypt(c3, key, n3)
print(f"Decrypt: {p3}")
