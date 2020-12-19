"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 1.py
Автор: 2020 © В.С. Свежинцев, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/12/2020
Дата последней модификации: 11/12/2020
Связанные файлы/пакеты: numpy, random
Описание:Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами элементы, стоящие на чётных и нечётных местах: A[1] ↔ A[2]; A[3] ↔ A[4] ...
#версия Python: 3.9.0
"""
import random
import sys

n = 25
a = [random.randint(0, 100) for i in range(0,n)]
print(a)
if (len(a) % 2 == 1):
    end = n
else:
    end = n-1
for i in range(0, end-1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
    
print(a)
