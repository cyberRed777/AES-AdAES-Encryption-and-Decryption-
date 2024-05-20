# AES-Encryption-and-Decryption-
These Python scripts demonstrate the use of Advanced Encryption Standard (AES) for encrypting and decrypting data. AES is a widely used symmetric-key block cipher that provides secure encryption and decryption of data.
aes_encrypt.py

This script generates a random 256-bit key and uses it to encrypt a plaintext message input by the user. The encrypted message is then saved to a file.

aes_decrypt.py

This script takes a key and an encrypted message as input from the user, and uses them to decrypt the message. The decrypted message is then printed to the console.

Key Generation

The scripts use the os module to generate a random 256-bit key, which is then used for encryption and decryption. The key is encoded in base64 format for easy storage and transmission.

Encryption and Decryption

The scripts use the cryptography library to perform AES encryption and decryption. The encryption algorithm used is AES-256-CBC, which is a widely used and secure encryption algorithm.

Security

The security of the encryption and decryption process relies on the secrecy of the key. It is essential to keep the key confidential and secure to prevent unauthorized access to the encrypted data.

Usage
	
