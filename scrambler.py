import json
import sys
import re
import random

"""Return random synonym, or same word."""
def randomize(word):
    if(word == "" or not word in thesaurus_dict.keys()):
        return word
    num = random.randint(0, len(thesaurus_dict[word]))
    # print("num = " + str(num))
    if(num == len(thesaurus_dict[word])):                      
        return word 
    return thesaurus_dict[word][num]

if(len(sys.argv) != 3):
    print("Usage: python3 scrambler.py <thesaurus> <plaintext>")
    quit()

thesaurus = sys.argv[1]
plaintext = sys.argv[2]

thesaurus_str = open(thesaurus, "r")
thesaurus_dict = json.loads(thesaurus_str.read())

unique_words = []
plaintext_str = open(plaintext, "r").read().lower()
plaintext_arr = re.compile(r'\w+').findall(plaintext_str)
unique_words = list(dict.fromkeys(plaintext_arr))

scrambled_message = ""
start = 0
end = 1
for i in range(0, len(plaintext_str)):
    if(plaintext_str[i].isalpha()):
        end = i
    else:
        scrambled_message += plaintext_str[start:start + 1]
        scrambled_message += randomize(plaintext_str[start + 1:end + 1])
        start = i
        end = i
                
print(scrambled_message)
