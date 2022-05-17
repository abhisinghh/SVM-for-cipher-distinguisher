import os
import binascii
from binascii import hexlify as hexa, unhexlify as unhexa, a2b_uu as bin_convert
import pandas as pd
import json

dictionary = {'0000' : 'a',\
'0001' : 'b',\
'0010' : 'c',\
'0011' : 'd',\
'0100' : 'e',\
'0101' : 'f',\
'0110' : 'g',\
'0111' : 'h',\
'1000' : 'i',\
'1001' : 'j',\
'1010' : 'k',\
'1011' : 'l',\
'1100' : 'm',\
'1101' : 'n',\
'1110' : 'o',\
'1111' : 'p'}

#print(dictionary)
# we will create fixed length word dictionary
K_BIT_SEQ = 4 #length of binary characters to make a symbol
CHAR_SEQ_LEN = 4 # length of symbols to make a word

dictionary_of_words = {}
set_of_words = set()

input_df = pd.read_csv("cipher_texts.csv")
#print(input_df.head())

cipher_texts = input_df.iloc[:1666,1]
print((cipher_texts))

def bin_to_symbol(data):
    sequenced_text = ''
    split = [data[i:i+K_BIT_SEQ] for i in range(0, len(data)-1, K_BIT_SEQ)]
    #print(len(split))
    for i in split :
        sequenced_text = sequenced_text + (dictionary[i])
        #print(sequenced_text)
    return sequenced_text
def symbol_to_word(data):
    split = [data[i:i+CHAR_SEQ_LEN] for i in range(0, len(data)-1, K_BIT_SEQ)]
    print(len(split),split)
    for i in range(len(split)) :
        if len(split[i]) != 4 : # will remove words with length != 4
            split.pop(i)
            #print(i)
    return split

for cipher_text in cipher_texts :
    #print(cipher_text)
    input =  cipher_text #input cipher text
    #print(input)
    #hex = hexa(input)  #not needed if input is already in hexa decimal format
    ct = unhexa(input)
    #print(len(ct), ct)
    #function to create symbols from binary data
    bin = ''   # stream that will store the binary string of cipher text
    symbol_str = '' #store symbols created from binary data
    for c in ct :
        bin_char = '{:08b}'.format(ord(c))
        bin += bin_char
        # print(ct)
    symbol_str = bin_to_symbol(bin)  # this will store the final stream of symbols created from binary string
    #print(symbol_str, len(symbol_str))
    #print(len(bin),(bin) )
    list_of_words = symbol_to_word(symbol_str)
    #print(list_of_words)

    for i in list_of_words :
        set_of_words.add(i)

print(len(set_of_words),set_of_words)
output_file = open('dictionary_for_aes.txt','a')
output_line = ''
for i in (set_of_words) :
    output_line = (i) + '\t'
    output_file.writelines(output_line)
output_file.close()
