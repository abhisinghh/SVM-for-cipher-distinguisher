
import os
from os import urandom
import encryption_algos


key = urandom(16)  #16 bytes = 128 bits
input = "helloyes"

aes = encryption_algos.aes_encryption_cbc()
ct = aes.encryptor(input, key)
print(ct)


blowfish = encryption_algos.blowfish_encryption_cbc()
ct = blowfish.encryptor(input, key)
print(ct)


des3_cbc = encryption_algos.des3_encryption_cbc()
ct = des3_cbc.encryptor(input, key)
print(ct)

des3_ecb = aes_imp_cbc_mode.des3_encryption_ecb()
ct = des3_ecb.encryptor(input, key)
print(ct)
