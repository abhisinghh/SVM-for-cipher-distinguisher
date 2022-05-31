
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa, unhexlify as unhexa
from os import urandom




#just for our understanding to see output in block format#
def blocks(data):
    split = [hexa(data[i:i+BLOCKLEN]) for i in range(0, len(data), BLOCKLEN)]

    return ' '.join(split)

#create a random key


class aes_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        #iv = urandom(16)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend = default_backend())
        aes_encrypt = cipher.encryptor()
        cipher_text = aes_encrypt.update(padded_data) + aes_encrypt.finalize()
        hexa_data = hexa(cipher_text)
        return hexa_data



class blowfish_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        #iv = urandom(8)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.Blowfish(key), modes.ECB(), backend = default_backend())
        des3_encrypt = cipher.encryptor()
        cipher_text = des3_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data


class des3_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        iv = urandom(8)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend = default_backend())
        des3_encrypt = cipher.encryptor()
        cipher_text = des3_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data


class des3_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend = default_backend())
        des3_encrypt = cipher.encryptor()
        cipher_text = des3_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data
