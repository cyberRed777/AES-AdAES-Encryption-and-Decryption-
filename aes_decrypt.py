from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def decrypt_message(key, encrypted_message):
    # Decode the base64-encoded string
    encrypted_message = base64.b64decode(encrypted_message)
    # Extract the IV from the encrypted message
    iv = encrypted_message[:16]
    encrypted_message = encrypted_message[16:]
    # Create a AES-256-CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    # Decrypt the message
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
    # Remove the padding
    decrypted_message = decrypted_message.decode().rstrip()
    return decrypted_message

# Get the key from the user
key = input("Enter the key (in hexadecimal format): ")
key = bytes.fromhex(key)

# Get the encrypted message from the user
encrypted_message = input("Enter the encrypted message (in base64 format): ")
encrypted_message = encrypted_message.encode()

# Decrypt the message
decrypted_message = decrypt_message(key, encrypted_message)
print("Decrypted Message:", decrypted_message)
