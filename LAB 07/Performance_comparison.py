import siphash
from Crypto.Hash import Poly1305, SHA256, SHA512
from Crypto.Cipher import AES
from Crypto import Random
import hmac
import time
from Crypto.Hash import CMAC


def main():
    # Initializations
    key = Random.get_random_bytes(16)
    msg = b"Benchmarking the performance of different MAC constructions"
    poly_key = Random.get_random_bytes(32)
    n = 10000

    print("=== HMAC 256 ===")
    start = time.time()
    for i in range(n):  # HMAC-256 n times
        hmac.new(key, msg=msg, digestmod=SHA256).hexdigest()

    print("Time:", time.time() - start)
    print()

    print("=== HMAC 512 ===")
    start = time.time()
    for i in range(n):  # HMAC-512 n times
        hmac.new(key, msg=msg, digestmod=SHA512).hexdigest()

    print("Time:", time.time() - start)
    print()

    print("=== Poly1305 ===")
    start = time.time()
    for i in range(n):  # Poly1305 n times
        Poly1305.new(key=poly_key, cipher=AES, data=msg)

    print("Time:", time.time() - start)
    print()

    print("===CMAC_AES_128===")
    start = time.time()
    for i in range(n):
        CMAC.new(key, ciphermod=AES, msg=msg)

    print("Time:", time.time() - start)
    print()

    print("===SipHash_2_4===")
    start = time.time()
    for i in range(n):
        siphash.SipHash_2_4(key, msg)

    print("Time:", time.time() - start)
    print()

    return 0


main()
