

key_1 = urandom(16)  #16 bytes = 128 bits

key_file = open('key.txt','a')

hexa_key = hexa(key_1)

key_file.writelines(hexa_key)

key_file.close()
