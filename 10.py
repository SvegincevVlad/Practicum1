"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 1.py
Автор: 2020 © В.С. Свежинцев, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/12/2020
Дата последней модификации: 11/12/2020
Связанные файлы/пакеты: numpy, random
Описание:Дано натуральное число. Определить, будет ли это число: чётным, кратным 10
#версия Python: 3.9.0
"""
num = int(input("Введите число для проверки:"))
if num % 2 == 0 and num % 10 == 0:
    print ("Число",num,"четно и кратно 10")
else:
    print("Число не соответсвует условию")
