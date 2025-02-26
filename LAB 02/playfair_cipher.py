import re

def prepare_text(text):
    # Remove non-alphabet characters and convert to uppercase
    text = re.sub(r'[^A-Za-z]', '', text).upper()
    # Replace 'J' with 'I' (standard in Playfair cipher)
    text = text.replace('J', 'I')
    # If two identical letters appear in the same digraph, insert 'X' between them
    text = re.sub(r'(.)\1', r'\1X\1', text)
    # If the length of the text is odd, append 'X' to make it even
    if len(text) % 2 != 0:
        text += 'X'
    return text

def generate_key_square(key):
    key = prepare_text(key)
    key_square = []
    used_letters = set()

    # Add key letters to the key square
    for letter in key:
        if letter not in used_letters:
            key_square.append(letter)
            used_letters.add(letter)

    # Add remaining letters of the alphabet (excluding 'J')
    for letter in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if letter not in used_letters:
            key_square.append(letter)

    # Convert the flat list into a 5x5 matrix
    key_matrix = [key_square[i * 5:(i + 1) * 5] for i in range(5)]
    return key_matrix

def find_position(key_square, letter):
    for row in range(5):
        if letter in key_square[row]:
            col = key_square[row].index(letter)
            return row, col
    return None

def encrypt_digraph(key_square, digraph):
    a, b = digraph[0], digraph[1]
    row_a, col_a = find_position(key_square, a)
    row_b, col_b = find_position(key_square, b)

    if row_a == row_b:
        # Same row: shift columns to the right (wrap around)
        return key_square[row_a][(col_a + 1) % 5] + key_square[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        # Same column: shift rows down (wrap around)
        return key_square[(row_a + 1) % 5][col_a] + key_square[(row_b + 1) % 5][col_b]
    else:
        # Rectangle: swap columns
        return key_square[row_a][col_b] + key_square[row_b][col_a]

def decrypt_digraph(key_square, digraph):
    a, b = digraph[0], digraph[1]
    row_a, col_a = find_position(key_square, a)
    row_b, col_b = find_position(key_square, b)

    if row_a == row_b:
        # Same row: shift columns to the left (wrap around)
        return key_square[row_a][(col_a - 1) % 5] + key_square[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        # Same column: shift rows up (wrap around)
        return key_square[(row_a - 1) % 5][col_a] + key_square[(row_b - 1) % 5][col_b]
    else:
        # Rectangle: swap columns
        return key_square[row_a][col_b] + key_square[row_b][col_a]

def encrypt_playfair(plaintext, key):
    key_square = generate_key_square(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ''

    for i in range(0, len(plaintext), 2):
        digraph = plaintext[i:i + 2]
        ciphertext += encrypt_digraph(key_square, digraph)

    return ciphertext

def decrypt_playfair(ciphertext, key):
    key_square = generate_key_square(key)
    plaintext = ''

    for i in range(0, len(ciphertext), 2):
        digraph = ciphertext[i:i + 2]
        plaintext += decrypt_digraph(key_square, digraph)

    return plaintext

key = "POLYBIUS"
plaintext = "THIS MESSAGE WAS ENCRYPTED WITH A GRID CIPHER"
ciphertext = encrypt_playfair(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt_playfair(ciphertext, key)
print("Decrypted Text:", decrypted_text)

# Display the key square
key_square = generate_key_square(key)
print("\nKey Square:")
for row in key_square:
    print(' '.join(row))
