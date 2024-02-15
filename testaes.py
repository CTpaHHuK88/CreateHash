from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def decrypt(ciphertext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Decrypt the ciphertext and remove the padding
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data
a = b'OO\xe1sU\xdd\xda\x88\x92.\xbc\x94Le\x83n\x91\xa3\xb9\x01\xe8\x02\x16NE\x88^\x10\x1c\x1ct\xfb6wg\x9eU\xf1\xec%\x17S\xe1T\xea\xa3\xc9\xb8'
b = '36bde8e0e31d1a661ec2a0fe4b8af5acb34525d09dd8559a51fa9f5424c23f2d'
decrypt(a, b)
