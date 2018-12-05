import string
import random

file_one_time_pad = open("encryption_file.txt","r")
p_text = file_one_time_pad.read()
file_one_time_pad.close()
print(p_text)
p_text = str.lower(p_text)
main_text = []
p_text_numerical = []
temp_key = [21,25,20,15,16,14,10,26,24,9,8,13]
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
main_key = []
cipher_text = []
cipher_text_numerical = []
length_p_text = len(p_text)
length_temp_key = len(temp_key)
random_alpha = 0
decipher_text = []
decipher_numerical = []



##Getting the numerical values of the text
for i in p_text:
	main_text.append(i)

for i in range(length_p_text):
	for j in range(25):
		if main_text[i] == alphabets[j]:
			p_text_numerical.append(j)
			break 


##Generating keys dynamically
if length_p_text == length_temp_key:
	for i in range(length_temp_key-1):
		main_key.append(temp_key[i])
elif length_p_text < length_temp_key:
	for i in range(length_p_text-1):
		main_key.append(temp_key[i])
else:
	for i in range(length_temp_key-1):
		main_key.append(temp_key[i])
	diff = length_p_text - length_temp_key
	for i in range(diff):
		random_alpha = random.choice(temp_key)
		main_key.append(random_alpha)
print("The main key is :: \n")
print(main_key)
print("The length of p_text_numerical::  \t",len(p_text_numerical))
print("\n")
print("The length of the main_key is :: \t",len(main_key))

## Ciphering algorithm

for i in range(length_p_text-1):
	cipher_text_numerical.append(abs(p_text_numerical[i]+main_key[i]))
print("The cipherred text is ::  \n")
print(cipher_text_numerical)


## Deciphering algorithm
length_cipher = len(cipher_text_numerical)
for i in range(length_cipher):
	decipher_numerical.append(cipher_text_numerical[i] - main_key[i])
print("The decipherred numerical::\n")
print(decipher_numerical)

temp = 0
for i in range(length_p_text-1):
	temp = decipher_numerical[i]	
	decipher_text.append(alphabets[temp])

deciphered_one = ""
for i in decipher_text:
	deciphered_one = deciphered_one + i

file_encrypt = open("encryption_file.txt","w")
file_encrypt.write(deciphered_one)
file_encrypt.close()
print("The deciphered text is ::\n")
print(decipher_text)


















