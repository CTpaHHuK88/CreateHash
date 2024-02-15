import hashlib

class HashGenSHA224(object):
    def __init__(self, message):
        self.message = message


        self.message = message
        hash_object = hashlib.sha224(self.message.encode())
        self.hex_dig = hash_object.hexdigest()
        print(self.hex_dig)
