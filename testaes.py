from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt(plaintext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the plaintext and encrypt it
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext


def decrypt(ciphertext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Decrypt the ciphertext and remove the padding
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data


# Example usage
plaintext = b"This is the message to be encrypted"
# Generate a random 256-bit (32-byte) key
# Key-length accepted: 16, 24, and 32 bytes.
key = b"3\x7f\xae\x11\x10\x81\xc2d\xdbo\xf7fM\xcch\xcb\xec\xed4\xda\x06\x88u\xc3\xaa'@F^\x8d\x11\xd4" # get_random_bytes(32)  # или генерируем рандомно keys/passphrase
print("Key:", key.hex())
# Encryption
encrypted_data = encrypt(plaintext, key)
print("Encrypted data:", encrypted_data)
# Decryption
decrypted_data = decrypt(encrypted_data, key)
print("Decrypted data:", decrypted_data)