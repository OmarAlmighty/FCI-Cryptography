from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256


def generate_key_pairs(curve='p256', passphrase="123"):
    # Generate public and private key pair
    keypair = ECC.generate(curve=curve)

    # Export the private key as PEM file and secure it with a passphrase
    with open("myprivatekey.pem", "wt") as f:
        data = keypair.export_key(format='PEM', passphrase=passphrase,
                                  protection='PBKDF2WithHMAC-SHA512AndAES256-CBC',
                                  prot_params={'iteration_count': 131072})
        f.write(data)

    # Export the public key as a PEM file
    with open("mypublickey.pem", "wt") as f:
        data = keypair.public_key().export_key(format='PEM')
        f.write(data)


def sign(data, private_key_file="myprivatekey.pem", passphrase="123"):
    # Hash the message using SHA256
    h = SHA256.new(data)
    # Import the private key
    with open(private_key_file, "rt") as f:
        key_file = f.read()
        key = ECC.import_key(key_file, passphrase)

    # Sign the message using a digital signature algorithm
    # The parameters are the private key and the mode
    # The fips-186-3 mode makes the signature randomized according to the FIPS standard
    # To make it deterministic use the 'deterministic-rfc6979' mode
    mydss = DSS.new(key, 'fips-186-3')

    signature = mydss.sign(h)
    return signature


def verify(data, signature, public_key_file="mypublickey.pem"):
    # Hash the message using SHA256
    h = SHA256.new(data)
    # Import the public key
    with open(public_key_file, "rt") as f:
        key_file = f.read()
        key = ECC.import_key(key_file)

    # Create a DSS object
    mydss = DSS.new(key, 'fips-186-3')

    try:
        # The verification algorithm takes the hash of the message
        # and the signature. If it's valid the program continues
        # Otherwise, it will throw an error
        mydss.verify(h, signature)
        print("Valid signature")
    except ValueError:
        print("Invalid signature")


data = b"This is my message to test ECDSA"
print(f"The data: {data}")
generate_key_pairs()
signature = sign(data)
print(f"The signature: {signature}")
verify(data, signature)
