from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

##from cryptography.fernet import Fernet
##import base64


# Creación de la clase de Codificación para DES
class DESEncode:
    def encrypt_data(self, data, key):
        cipher = DES.new(key, DES.MODE_ECB)
        plaintext = pad(data.encode(), DES.block_size)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext

##    def encrypt(self, encrypted_data, key):
##        llave = Fernet.generate_key(key)
##        cipher_suite: Fernet = Fernet(llave)
##        encrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')
##        return encrypted_data
