import hashlib

class HashGenSHA256(object):
    def __init__(self, salt, message):
        self.message = message
        self.salt = salt
        self.passw = salt + message

        hash_object = hashlib.sha256(self.passw.encode())
        self.hex_dig = hash_object.hexdigest()
        print(self.hex_dig)



