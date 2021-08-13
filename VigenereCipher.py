#Ask user to type in a string and a key, and then encrypt the string by the key

import re

message = input("What is the message that you want to encrypt?").lower() #the original message to be encrypted
len_m = len(message)
en_message = "" #the encrypted message
de_message = "" #the decrypted message
key = "1"

#Make sure that the key is valid
def valid_key(k):
    regular_expression = re.compile(r"[^a-zA-Z.]")
    k = regular_expression.search(k)
    return not bool(k)

while not valid_key(key):
    print("A valid key should consist only of letters.")
    key = input("Please enter a key.").lower() #the key
key = key*(len_m//len(key)+1)
key = key[:len_m]

#encrypt the message
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(len_m):
    if message[i] not in letters:
        en_message+=message[i]
    else:
        index_message = letters.find(message[i])
        index_key = letters.find(key[i])
        if index_message >=0:
            en_message += letters[(index_message +index_key) % 26]
        else:
            en_message += message[i]

#decrypt the message
for i in range (len(en_message)):
    if en_message[i] not in letters:
        de_message+=message[i]
    else:
        index_en = letters.find(en_message[i])
        index_key = letters.find(key[i])
        if index_en >=0:
            de_message += letters[(index_en - index_key) % 26]
        else:
            de_message += en_message[i]

#print the outcome
print ("The original message is:", message)
print ("The key is:", key)
print ("The encrypted message is:", en_message)
print ("The decrypted message is:", de_message)
