import hashlib

ha = '69972fa6d70f87bde4c0f09d7a736bda4b040a33e6cefd22887897c1d1ea8d28'


md5_hash_new = hashlib.md5(ha).hexdigest()

print(md5_hash_new)