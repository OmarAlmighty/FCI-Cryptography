import random
from sympy import isprime
from math import gcd


# Function to generate a large prime number
def generate_prime(bitsize):
    while True:
        num = random.getrandbits(bitsize)
        if isprime(num):
            return num


# Function to compute the modular inverse (extended Euclidean algorithm)
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


# Function to generate RSA keys
def generate_rsa_keys(bitsize=2048):
    # Step 1: Generate two distinct large prime numbers p and q
    p = generate_prime(bitsize // 2)  # half the bitsize for p
    q = generate_prime(bitsize // 2)  # half the bitsize for q

    # Step 2: Compute n = p * q
    n = p * q

    # Step 3: Compute Euler's totient function phi(n) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)

    # Step 4: Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 65537  # Common choice for e
    # while gcd(e, phi_n) != 1:
    #     e = random.randrange(2, phi_n)

    # Step 5: Compute d such that e * d ≡ 1 (mod phi(n)) - the modular inverse of e
    d = modinv(e, phi_n)

    # Public key (e, n)
    public_key = (e, n)

    # Private key (d, n)
    private_key = (d, n)

    return private_key, public_key


def rsa_encrypt(message, public_key):
    e = public_key[0]
    n = public_key[1]
    # pow() is a fast modular exponentiation function built-in python
    ctxt = pow(message, e, n)
    return ctxt


def rsa_decrypt(message, private_key):
    d = private_key[0]
    n = private_key[1]
    # pow() is a fast modular exponentiation function built-in python
    ptxt = pow(message, d, n)
    return ptxt


# Example usage
private_key, public_key = generate_rsa_keys(bitsize=2048)

print("Private Key: ", private_key)
print("Public Key: ", public_key)

msg = 45
encrypted = rsa_encrypt(msg, public_key)
print("Encrypted Message: ", encrypted)
decrypted = rsa_decrypt(encrypted, private_key)
print("Decrypted Message: ", decrypted)
