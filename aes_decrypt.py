
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

password = "Abghfgta@@@#@@@hffdjknjkf78676HHgdfbd^^^hbfvdjklf.gkjnfgkjhn534561215gfhngfkjnjbnnbi8988787%^%^&%^^%jhjkhjklbjklb4556bnjklbnflb8678678687786798"

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


aes_encrypted = open("encryption_file.txt","r")
aes_encrypted_text = aes_encrypted.read()
aes_encrypted.close()

decrypted = decrypt(aes_encrypted_text, password)

aes_file_decode = open("encryption_file.txt","w")
aes_file_decode.write(decrypted.decode())
aes_file_decode.close()

print(bytes.decode(decrypted))
