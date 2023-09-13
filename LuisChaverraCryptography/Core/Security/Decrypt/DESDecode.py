from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad

##from cryptography.fernet import Fernet

#Creación de la clase de Codificación para DES
class DESDecode:
    def decrypt_data(ciphertext, key):
        cipher = DES.new(key, DES.MODE_ECB)
        decrypted_data = cipher.decrypt(ciphertext)
        plaintext = unpad(decrypted_data, DES.block_size)
        return plaintext.decode()
##    def decrypt(self, data, key):
##        self.key = key.encode('utf-8')  # Convierte la clave en bytes
##        self.cipher_suite = Fernet(self.key)
##        encrypted_data = self.cipher_suite.encrypt(data.encode('utf-8'))
##        return encrypted_data