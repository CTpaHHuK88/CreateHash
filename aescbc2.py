from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode
from Crypto.Util.Padding import unpad

sensitive_data = b"#EdrtFTg*&9sf"
key = b'\x8f\xe59\xb5\xbd\x804aj\xc6\xed\x0f\xb1bS\xa0\x10\x8b\xcbz\x02\xe6\x8dW\xd95\xd5.\x18o`\xd5' #get_random_bytes(32) #must be 16, 24 or 32 bytes long
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(sensitive_data, AES.block_size))

i = b64encode(cipher.iv).decode('utf-8')
c = b64encode(ciphertext).decode('utf-8')
k = b64encode(key).decode('utf-8')

print(f"iv: {b64encode(cipher.iv).decode('utf-8')}")
print(f"ciphertext:{b64encode(ciphertext).decode('utf-8')}")
print(f"key: {b64encode(key).decode('utf-8')}")



try:
    iv = b64decode(f'{i}')
    ciphertext = b64decode(f'{c}')
    key = b64decode(f'{k}')
#    key = b64decode(b'\x83\xe5\xe9\xae\xb7\x05\x9aD<\x9c%BJ\xc8\n\xde\x8d\xe5"\xc8&K\xea\x05\x06X\x9e\\\xd54t\xd9')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print("Original Message was: ", plaintext)
except (ValueError, KeyError):
    a = ValueError
    print("ERROR!")

#a_ciphertext = b64decode('0W6tw7CduTlymN8tOeWAL4UhCuu0ItyV7oZ7q3JWx3k=')
#b_iv = b64decode('V3/oW179L1BRtRP11Nfc/w==')
#c_key = b64decode('jbFlVdSLxI7kWkQTTjvoyQ==')

#print(a_ciphertext, b_iv, c_key)