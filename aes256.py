from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(32)   
cipher = AES.new(key, AES.MODE_CBC)

plaintext = b"HELLO THIS IS SECRET DATA"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print(ciphertext)
