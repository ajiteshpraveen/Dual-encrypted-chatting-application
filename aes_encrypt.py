import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

password = "Abghfgta@@@#@@@hffdjknjkf78676HHgdfbd^^^hbfvdjklf.gkjnfgkjhn534561215gfhngfkjnjbnnbi8988787%^%^&%^^%jhjkhjklbjklb4556bnjklbnflb8678678687786798"


def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


rail_encrypted = open("encryption_file.txt","r")
rail_encrypted_text = rail_encrypted.read()
rail_encrypted.close()

encrypted = encrypt(rail_encrypted_text, password)

file_aes = open("encryption_file.txt","w")
file_aes.write(encrypted.decode())
file_aes.close()
print(encrypted)


