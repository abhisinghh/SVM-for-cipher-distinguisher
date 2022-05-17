
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa, unhexlify as unhexa
from os import urandom


BLOCKLEN = 16 #16 bytes

#just for our understanding to see output in block format#
def blocks(data):
    split = [hexa(data[i:i+BLOCKLEN]) for i in range(0, len(data), BLOCKLEN)]

    return ' '.join(split)

#create a random key
key = urandom(16)  #16 bytes = 128 bits

#print("key = %s" %hexa(key))

# initializing vector
iv = urandom(8)
#creating instance of AES-128 with CBC mode

#plaintexts from file
input_file = open('plain_texts.txt','r')
input_plain_texts = []

counter = 0
for readline in input_file :
    pt = readline.strip()
    if counter <= 66 :
        counter += 1
    elif counter > 66 and counter <= 99 :
        counter += 1
        input_plain_texts.append(pt)
    else :
        break

input_file.close()
cipher_texts = []
encryption_algorithm = []
decrypted_texts = []
length_input_text = []
length_cipher_text = []
length_decrypted_text  = []
for plain_text in input_plain_texts :
    #plain_text = 'ABCDEFGHAB'
    encryption_algorithm.append('Blowfish')
    #print("plain text = %s" %plain_text)
    print("length of plain text = %s" %len(plain_text))

    length_input_text.append(len(plain_text))

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plain_text) + padder.finalize()
    #print(plain_text, padded_data, hexa(padded_data), len(padded_data))
    #print(hexa(padded_data))

    #encrypt plaintext p to ciphertext c
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend = default_backend())
    des3_encrypt = cipher.encryptor()
    cipher_text = des3_encrypt.update(padded_data) + des3_encrypt.finalize()

    #print("enc(%s) = %s" %(blocks(padded_data), blocks(cipher_text)))

    #print("Cipher text = %s" %cipher_text)
    print("length of Cipher text = %s" %len(cipher_text))

    cipher_texts.append(cipher_text)
    length_cipher_text.append(len(cipher_text))
    #decrypt ciphertext c to plaintext p
    des3_decrypt = cipher.decryptor()
    decrypted_text = des3_decrypt.update(cipher_text) + des3_decrypt.finalize()
    #print("dec(%s) = %s" % (blocks(cipher_text), blocks(decrypted_text)))

    #print("Decrypted text = %s" %((decrypted_text)))

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_text) + unpadder.finalize()

    #print("Decrypted text = %s" %(unpadded_data))
    print("length of Decrypted text = %s" %len(unpadded_data))

    decrypted_texts.append(unpadded_data)
    length_decrypted_text.append(len(unpadded_data))

output_file = open('cipher_texts.txt','a')
#output_file.writelines('sr_no\tinput_text\tlength_input_text\tcipher_text\t\
#length_cipher_text\tdecrypted_text\tlength_decrypted_text\n')

for i in range(33) :
    output_line = str(i) +'\t'+ str(input_plain_texts[i]) + '\t' + str(length_input_text[i]) + '\t' + \
    str(hexa(cipher_texts[i])) + '\t' + str(length_cipher_text[i]) + '\t' + str(decrypted_texts[i]) + '\t'+ str(length_decrypted_text[i]) + '\n'
    output_file.writelines(output_line)
output_file.close()
