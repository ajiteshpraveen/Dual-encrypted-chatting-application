import socket
import subprocess


s = socket.socket()          
print ("Socket successfully created")
port = 8080               
s.bind(('', port))         
print ("socket binded to %s" %(port))  
s.listen(5)      
print ("socket is listening")
while True:
	c, addr = s.accept()
	cipher_text = (c.recv(1024)).decode("utf-8")
	file_cipher_text = open("encryption_file.txt","w")
	file_cipher_text.write(cipher_text)
	file_cipher_text.close()
	subprocess.check_call(["python3", "aes_decrypt.py"])
	subprocess.check_call(["python3", "rail_fence_decipher.py"])

	file_decode = open("decoded_text.txt","r")
	t = file_decode.read()
	file_decode.close()
	print(t) 

	msg = input("Server message: ")   
	file_plain = open("plain_text.txt","w")
	file_plain.write(msg)		
	file_plain.close()	
	subprocess.check_call(["python3", "rail_fence.py"])
	subprocess.check_call(["python3", "aes_encrypt.py"])
	file_cipher = open("encryption_file.txt","r")
	encrypted_text = file_cipher.read()
	file_cipher.close()
	c.send(bytes(encrypted_text,"utf8"))
	c.close() 

