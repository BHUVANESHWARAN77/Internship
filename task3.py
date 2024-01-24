
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

class FileEncryptor:
    def __init__(self, key):
        self.key = base64.urlsafe_b64encode(key)[:32]  # Use first 32 bytes for AES-256

    def _pad_data(self, data):
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        return padder.update(data) + padder.finalize()

    def _unpad_data(self, data):
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        return unpadder.update(data) + unpadder.finalize()

    def encrypt_file_aes(self, input_file, output_file):
        with open(input_file, 'rb') as file:
            plaintext = file.read()

        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()

        encrypted_data = encryptor.update(self._pad_data(plaintext)) + encryptor.finalize()

        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file_aes(self, input_file, output_file):
        with open(input_file, 'rb') as file:
            encrypted_data = file.read()

        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_data = self._unpad_data(decryptor.update(encrypted_data) + decryptor.finalize())

        with open(output_file, 'wb') as file:
            file.write(decrypted_data)

    def encrypt_file_des(self, input_file, output_file):
        # Implement DES encryption here
        pass

    def decrypt_file_des(self, input_file, output_file):
        # Implement DES decryption here
        pass

# Example usage
key = os.urandom(32)  # Generate a random 32-byte key

file_encryptor = FileEncryptor(key)

# Encrypt a file using AES
file_encryptor.encrypt_file_aes('plaintext.txt', 'encrypted_aes.bin')

# Decrypt the AES-encrypted file
file_encryptor.decrypt_file_aes('encrypted_aes.bin', 'decrypted_aes.txt')
