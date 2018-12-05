## Deciphering algorithm
length_cipher = len(cipher_text_numerical)
for i in range(length_cipher):
	decipher_numerical.append(cipher_text_numerical[i] - main_key[i])
print("The decipherred numerical::\n")
print(decipher_numerical)

temp = 0
for i in range(length_p_text):
	temp = decipher_numerical[i]	
	decipher_text.append(alphabets[temp])

print("The deciphered text is ::\n")
print(decipher_text)



