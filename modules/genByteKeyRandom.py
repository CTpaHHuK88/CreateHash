import random

#Генерируем ключ 32 byte
def genByteKeyRandom():
    key = random.randbytes(32)
    return key

print(genByteKeyRandom())