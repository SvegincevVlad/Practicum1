"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 1.py
Автор: 2020 © В.С. Свежинцев, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/12/2020
Дата последней модификации: 11/12/2020
Связанные файлы/пакеты: numpy, random
Описание:Определить значение функции Z = 1/(XY ) при произвольных X и Y 
#версия Python: 3.9.0
"""
x = int(input("Введите Х:"))
y = int(input("Введите У:"))
z = 1 / (x*y)
print("Значение ф-ии равно",z)