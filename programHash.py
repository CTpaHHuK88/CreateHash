from modules import hashGenSHA1
from modules import hashGenSHA224
from modules import hashGenSHA256
from modules import hashGenSHA512



print("Выберите алгоритм шифрования:")
print("1 - SHA1")
print("2 - SHA224")
print("3 - SHA256")
print("4 - SHA512")

number = int(input(""))

try:

    if number == 1:
        print("Вы выбрали алгоритм SHA1")
        a = input("Введите данные для шифрования алгоритмом SHA1:")
        hashGenSHA1.HashGenSHA1(a)
    if number == 2:
        print("Вы выбрали алгоритм SHA224")
        b = input("Введите данные для шифрования алгоритмом SHA1:")
        hashGenSHA224.HashGenSHA224(b)
    if number == 3:
        print("Вы выбрали алгоритм SHA256")
        c = input("Введите данные для шифрования алгоритмом SHA256:")
        hashGenSHA256.HashGenSHA256(c)
    if number == 4:
        print("Вы выбрали алгоритм SHA512")
        d = input("Введите данные для шифрования алгоритмом SHA256:")
        hashGenSHA512.HashGenSHA512(d)
except:
    if number > 4:
        print("Выберите правильный вариант.")