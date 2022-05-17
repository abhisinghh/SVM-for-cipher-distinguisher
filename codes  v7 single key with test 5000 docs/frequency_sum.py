import os
import pandas as  pd

aes_dict = pd.read_csv('dictionary_for_aes.txt', '\t')
print(aes_dict.shape)


des3_dict = pd.read_csv('dictionary_for_3des.txt', '\t')
print(des3_dict.shape)


blowfish_dict = pd.read_csv('dictionary_for_blowfish.txt', '\t')
print(blowfish_dict.shape)


total_sum = X.sum(axis=1)
print(total_sum)
df_aes_output['sum_of_freq'] = total_sum
