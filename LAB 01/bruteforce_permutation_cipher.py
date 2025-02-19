from itertools import permutations


# Function to generate a random permutation key of a given size.
def get_possible_keys(size=3):
    permuts = list(permutations(range(size)))
    return permuts


# Function to calculate the inverse of a permutation key.
# The inverse key maps the positions back to their original indices.
def inv_key(key):
    ik = list(range(len(key)))  # Initialize a list of indices from 0 to len(key)-1
    for i in range(len(key)):  # Iterate over each index in the key
        k = key[i]  # The value of key[i] is the new position of the element i in the original list
        ik[k] = i  # Set the inverse key's value at position k to i (inverse mapping)
    return ik


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


ctxt = "CIFLN0{TS3_CR3U}"
keylen = 2
for i in range(len(ctxt) - 2):
    keys = get_possible_keys(keylen + i)
    for k in keys:
        ptxt = permutation_decrypt(ctxt, k)
        print("(", k, ")", ptxt)
        # if ptxt.startswith("FCIL"):
        #     exit(0)
