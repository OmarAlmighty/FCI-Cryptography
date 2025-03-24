import random
from sympy import isprime


def generate_prime(bitsize):
    while True:
        num = random.getrandbits(bitsize)
        if isprime(num):
            return num

def find_generator(p):
    """Find a generator for cyclic group Zp*"""
    phi = p - 1
    for alpha in range(2, p):
        if pow(alpha, phi, p) == 1:  # Basic check for generator
            return alpha
    return None


def generate_elgamal_keys(bits=256):
    # Generate large prime p
    p = generate_prime(bits)
    # Find generator alpha
    alpha = find_generator(p)
    # Private key (random number less than p-1)
    x = random.randint(1, p - 2)
    # Public key K = alpha^x mod p
    K = pow(alpha, x, p)
    public_key = (p, alpha, K)
    private_key = (x, p)
    return public_key, private_key


def elgamal_encrypt(public_key, msg):
    p, alpha, K = public_key
    # Random k
    k = random.randint(1, p - 2)
    # c1 = alpha^k mod p
    c1 = pow(alpha, k, p)
    # c2 = K^k * m mod p
    c2 = (pow(K, k, p) * msg) % p
    return c1, c2


def elgamal_decrypt(private_key, ctxt):
    c1, c2 = ctxt
    x, p = private_key
    # s = c1^x mod p
    s = pow(c1, x, p)
    # m = c2 * s^-1 mod p
    # s^-1 is the modular multiplicative inverse of s modulo p
    s_inv = pow(s, -1, p)  # Using Python's built-in modular inverse
    m = (c2 * s_inv) % p
    return m


# Get public key
public_key, private_key = generate_elgamal_keys()
print(f"Public key (p, alpha, K): {public_key}")
print(f"Private key (x): {private_key}")

# Example message (must be integer < p)
message = 42
print(f"Original message: {message}")

# Encrypt
ciphertext = elgamal_encrypt(public_key, message)
print(f"Ciphertext (c1, c2): {ciphertext}")

# Decrypt
decrypted = elgamal_decrypt(private_key, ciphertext)
print(f"Decrypted message: {decrypted}")
