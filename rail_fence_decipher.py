file_cipher_text = open("encryption_file.txt","r")
ciphered_text = file_cipher_text.read()
file_cipher_text.close()		
##Decipher algortihm
d_cipher = []	
decipher_text = ""
a = 0 
b = 1
c = 2
count = 0

for i in ciphered_text:
	d_cipher.append(i)	

length_d_cipher = len(d_cipher)
d_arr1 = [None] * length_d_cipher
d_arr2 = [None] * length_d_cipher
d_arr3 = [None] * length_d_cipher
count = 0

for j in d_cipher:
	if a < length_d_cipher:
		d_arr1[a] = j
		count = count + 1
	a = a + 4
	

for j in range(length_d_cipher):
	if b < length_d_cipher and count < length_d_cipher:
		d_arr2[b] = d_cipher[count]
		b = b + 2
		count = count + 1


for j in range(length_d_cipher):
	if c < length_d_cipher and count < length_d_cipher:
		d_arr3[c] = d_cipher[count]
		c = c + 4
		count = count + 1

d_arr11 = []
d_arr22 = []
d_arr33 = []

## Use these for further proceedings
for i in d_arr1:
	if i != None:
		d_arr11.append(i)

for j in d_arr2:
	if j != None:	
		d_arr22.append(j)

for k in d_arr3:
	if k != None:	
		d_arr33.append(k)



print(d_arr11)
print(d_arr22)
print(d_arr33)
length_d_arr11 = len(d_arr11)
length_d_arr22 = len(d_arr22)
length_d_arr33 = len(d_arr33)

mid_row = 0
for i in range(length_d_cipher):
	if i < length_d_arr11:
		decipher_text = decipher_text + d_arr11[i] 	

	if mid_row < length_d_arr22:
		decipher_text = decipher_text + d_arr22[mid_row]

	if i < length_d_arr33:
		decipher_text = decipher_text + d_arr33[i]
	
	mid_row = mid_row + 1
	
	if mid_row < length_d_arr22:
		decipher_text = decipher_text + d_arr22[mid_row]
		
	mid_row = mid_row + 1



print("The deciphered text is :: \n")
print(decipher_text)

file_cipher = open("decoded_text.txt","w")
file_cipher.write(decipher_text)
file_cipher.close()


