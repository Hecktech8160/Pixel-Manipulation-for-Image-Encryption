"""Develope a simple image encryption tool uding pixel manipulation."""
"""User can perform operations like swapping,pixel values,and applying a basic mathematical operation to each pixel."""
"""Allow user to encrypt and decrypt images."""
from cryptography.fernet import Fernet
import os

# Function to generate a key and save it into a file
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key():
    return open('secret.key', 'rb').read()

# Function to encrypt a file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)
    
    encrypted_path = file_path + '.enc'
    with open(encrypted_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    print(f"File {file_path} encrypted and saved as {encrypted_path}")
    return encrypted_path

# Function to decrypt a file
def decrypt_file(encrypted_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(encrypted_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    
    decrypted_path = encrypted_path.replace('.enc', '_decrypted')
    with open(decrypted_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    
    print(f"File {encrypted_path} decrypted and saved as {decrypted_path}")
    return decrypted_path

# Generate key only once and save it
if not os.path.exists('secret.key'):
    generate_key()

# Ask the user for the file path to encrypt
file_path = input("Enter the path of the file you want to encrypt: ")

# Encrypt the file
encrypted_file_path = encrypt_file(file_path)

# Ask the user if they want to decrypt the file
decrypt_choice = input("Do you want to decrypt the file? (yes/no): ")

if decrypt_choice.lower() == 'yes':
    # Decrypt the file
    decrypted_file_path = decrypt_file(encrypted_file_path)
