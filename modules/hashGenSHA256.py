import hashlib

class HashGenSHA256(object):
    def __init__(self, message):
        self.message = message


        self.message = message
        hash_object = hashlib.sha256(self.message.encode())
        self.hex_dig = hash_object.hexdigest()
        print(self.hex_dig)



