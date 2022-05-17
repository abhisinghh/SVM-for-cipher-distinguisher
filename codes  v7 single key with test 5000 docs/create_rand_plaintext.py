import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    #print("Random string of length", length, "is:", result_str)
    return result_str

#str = get_random_string(50)

output_file = open('plain_texts.txt','a')

for i in range(5000) :
    print(i)
    str = get_random_string(500)
    output_line = str +'\n'
    if i == 99 :
        output_line = str
    output_file.writelines(output_line)
output_file.close()


output_file = open('test_plain_texts.txt','a')

for i in range(5000) :
    print(i)
    str = get_random_string(500)
    output_line = str +'\n'
    if i == 99 :
        output_line = str
    output_file.writelines(output_line)
output_file.close()
