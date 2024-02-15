from modules import hashGenSHA256



print("Выберите алгоритм шифрования:")
print("1 - SHA1")
print("2 - SHA224")
print("3 - SHA256")
print("4 - SHA512")

number = int(input(""))

try:

    if number == 1:
        print("Вы выбрали алгоритм SHA1")

    if number == 2:
        print("Вы выбрали алгоритм SHA224")
    if number == 3:
        print("Вы выбрали алгоритм SHA256")
        a = input("Введите данные для шифрования алгоритмом SHA256:")
        hashGenSHA256.HashGenSHA256(a)


    if number == 4:
        print("Вы выбрали алгоритм SHA512")
except:
    if number > 4:
        print("Выберите правильный вариант.")