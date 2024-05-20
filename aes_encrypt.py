from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_key():
    # Generate a 256-bit key
    key = os.urandom(32)
    return key

def encrypt_message(key, message):
    # Create a random 128-bit IV
    iv = os.urandom(16)
    # Create a AES-256-CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Pad the message to a multiple of the block size
    padded_message = message + ' ' * (16 - len(message) % 16)
    # Encrypt the message
    encrypted_message = encryptor.update(padded_message.encode()) + encryptor.finalize()
    # Return the IV and encrypted message as a base64-encoded string
    return base64.b64encode(iv + encrypted_message)

# Generate a key
key = generate_key()
print("Key:", key.hex())

# Get the plaintext from the user
message = input("Enter the plaintext: ")

# Encrypt the message
encrypted_message = encrypt_message(key, message)
print("Encrypted Message:", encrypted_message)

# Save the encrypted message to a file
with open("encrypted_message.txt", "wb") as f:
    f.write(encrypted_message)
