"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 1.py
Автор: 2020 © В.С. Свежинцев, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/12/2020
Дата последней модификации: 11/12/2020
Связанные файлы/пакеты: numpy, random
Описание:Дано натуральное число. Определить, будет ли это число: нечётным, кратным 7.
#версия Python: 3.9.0
"""
num = int(input("Введите число для проверки:"))
if num % 2 == 1 and num % 7 == 0:
    print("Число", num, "нечетно и кратно 7")
else:
    print("Число не соответсвует условию")