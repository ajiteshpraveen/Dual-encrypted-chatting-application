file_plain_text = open("plain_text.txt","r")
p_text = file_plain_text.read()
file_plain_text.close()
depth = 3
text_modified = "" 

for each_letter in p_text:
	text_modified = text_modified + each_letter

if len(text_modified) == 2:
	text_modified = text_modified + "x" + "x"
	
print ("The modified string is :  ",text_modified)

length_modified_text = len(text_modified)

arr = []

#Converting modified string into array

for i in text_modified:
	arr.append(i)

arr_1 = []
arr_2 = []
arr_3 = []
length_arr = len(arr)

i = 0
j = 1
k = 2
check  = 0

#Main Algorithm  -- Rail Fence Implementation
while i <= length_arr:
	if i < length_arr:
		arr_1.append(arr[i])
	i = i + 4
			
while j <= length_arr:
	if j < length_arr:
		arr_2.append(arr[j])
	j = j + 2

while k < length_arr:
	if k <= length_arr:
		arr_3.append(arr[k])
	k = k + 4	

print(arr_1)
print("\n")
print(arr_2)
print("\n")
print(arr_3)


# Arranging the encrypted text
ciphered_text = ""

for i in arr_1:
	ciphered_text = ciphered_text + i


for i in arr_2:
	ciphered_text = ciphered_text + i


for i in arr_3:
	ciphered_text = ciphered_text + i


#Printing the ciphered text and writing it into a file	
file_cipher = open("encryption_file.txt","w")
file_cipher.write(ciphered_text)
file_cipher.close()	
print("The ciphered text is : \n")
print(ciphered_text)
		

