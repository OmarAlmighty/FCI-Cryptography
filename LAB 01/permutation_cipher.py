import random
from itertools import permutations


# Function to generate a random permutation key of a given size.
def get_key(size=3):
    permuts = list(permutations(range(size)))
    return permuts[random.randint(1, len(permuts) - 1)]


# Function to calculate the inverse of a permutation key.
# The inverse key maps the positions back to their original indices.
def inv_key(key):
    ik = list(range(len(key)))  # Initialize a list of indices from 0 to len(key)-1
    for i in range(len(key)):  # Iterate over each index in the key
        k = key[i]  # The value of key[i] is the new position of the element i in the original list
        ik[k] = i  # Set the inverse key's value at position k to i (inverse mapping)
    return ik


# Function to encrypt a message using a permutation cipher.
# The plaintext is divided into blocks of the size of the key, and each block is permuted according to the key.
def permutation_encrypt(plaintext, key):
    keylen = len(key)  # The size of the permutation key (i.e., the length of each block)

    # Ensure the plaintext length is a multiple of the key length by padding with "-"
    while len(plaintext) % keylen != 0:
        plaintext += "-"  # Append "-" to the plaintext until its length is a multiple of keylen

    ptxt_blocks = []  # List to hold blocks of the plaintext
    # Split the plaintext into blocks of the appropriate size
    for block in range(0, len(plaintext), keylen):
        ptxt_blocks.append(plaintext[block:block + keylen])

    ctxt_blocks = [''] * len(ptxt_blocks)
    # Permute each block according to the key
    for block in ptxt_blocks:
        permuted = [''] * len(key)  # Create a list of empty strings to hold the permuted block
        for i in range(len(block)):  # Loop through each character in the block
            permuted[key[i]] = block[i]  # Place the character at the new position given by the key

        permuted = "".join(permuted)  # Join the permuted characters to form a string (a permuted block)
        ctxt_blocks.append(permuted)  # Append the permuted block to the ciphertext blocks list

    return "".join(ctxt_blocks)  # Join all the ciphertext blocks together and return as a single string


# Function to decrypt a message encrypted using a permutation cipher.
# It uses the inverse of the encryption key to reverse the permutation.
def permutation_decrypt(ciphertext, key):
    keylen = len(key)
    key = inv_key(key)

    ctxt_blocks = []
    # Split the ciphertext into blocks of the appropriate size
    for block in range(0, len(ciphertext), keylen):
        ctxt_blocks.append(ciphertext[block:block + keylen])

    ptxt_blocks = [''] * len(ctxt_blocks)
    # Reverse the permutation for each block using the inverse key
    for block in ctxt_blocks:
        permuted = [''] * len(key)  # Create a list of empty strings to hold the permuted block
        for i in range(len(block)):  # Loop through each character in the block
            permuted[key[i]] = block[i]  # Place the character at the position specified by the inverse key

        permuted = "".join(permuted)  # Join the permuted characters to form a string (a permuted block)
        ptxt_blocks.append(permuted)  # Append the permuted block to the plaintext blocks list

    return "".join(ptxt_blocks)  # Join all the plaintext blocks together and return as a single string


msg = "THIS MESSAGE IS ENCRYPTED WITH A TRANSPOSITION CIPHER"
key = get_key(5)
print(key)
ctxt = permutation_encrypt(msg, key)
print(ctxt)
ptxt = permutation_decrypt(ctxt, key)
print(ptxt)
