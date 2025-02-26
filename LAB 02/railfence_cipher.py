def railfence_encrypt(plaintext, num_rails, offset=0):
    ciphertext = [["-"] * (len(plaintext) + offset)] * num_rails  # Initialize the grid for cipher
    tmp_offset = offset  # Keep track of remaining offset
    rail = 0  # Start at the first rail
    move = 1  # Set the initial direction to "down"
    for i in range(len(plaintext) + offset):
        tmp = ciphertext[rail].copy()  # Make a copy of the current rail's list
        # If there's still offset to handle, place "#" on the grid
        if tmp_offset > 0:
            tmp[i] = "#"
            ciphertext[rail] = tmp  # Update the rail with the modified list
            tmp_offset -= 1  # Decrease remaining offset
            if rail == num_rails - 1:  # If bottom rail is reached, change direction
                move *= -1
            rail += move  # Move to the next rail in the correct direction
            if rail == 0:  # If top rail is reached, change direction
                move *= -1
            continue

        # Place the actual character in the grid
        tmp[i] = plaintext[i - offset]
        # Update the current rail
        ciphertext[rail] = tmp

        if rail == num_rails - 1:  # If bottom rail is reached, change direction
            move *= -1

        rail += move  # Move to the next rail in the current direction

        # If top rail is reached, change direction
        if rail == 0:
            move *= -1

    return ciphertext


def railfence_decrypt(ciphertext, num_rails, offset=0):
    plaintext = ""
    rail = 0
    move = 1
    # Loop through each column
    for i in range(len(ciphertext[0])):
        tmp = ciphertext[rail].copy()  # Copy current rail's list
        plaintext += tmp[i]  # Append character from the current rail to the plaintext
        if rail == num_rails - 1:  # If bottom rail is reached, change direction
            move *= -1

        rail += move  # Move to the next rail in the correct direction

        if rail == 0:  # If top rail is reached, change direction
            move *= -1

    return plaintext


def print_ciphertext(ciphertext):
    ctxt = ""
    for i in range(len(ciphertext)):  # Loop through each rail
        tmp = "".join(ciphertext[i])  # Join the elements of the rail into a string
        ctxt += tmp  # Append the row's string to the complete ciphertext
        print(tmp)  # Print the row of the ciphertext

    ctxt = ctxt.replace("-", "")  # Remove placeholders
    ctxt = ctxt.replace("#", "")
    print(ctxt)  # Print the final ciphertext without placeholders


def print_plaintext(plaintext):
    ptxt = plaintext.replace("-", "")
    ptxt = ptxt.replace("#", "")
    print(ptxt)


ptxt = "THIS MESSAGE WAS ENCRYPTED WITH A TRANSPOSITION CIPHER"

ctxt = railfence_encrypt(ptxt, 4, 5)
print_ciphertext(ctxt)

decrypted = railfence_decrypt(ctxt, 4, 5)
print_plaintext(decrypted)
