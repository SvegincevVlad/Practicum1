"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 1.py
Автор: 2020 © В.С. Свежинцев, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/12/2020
Дата последней модификации: 11/12/2020
Связанные файлы/пакеты: numpy, random
Описание:
#версия Python: 3.9.0
"""
import random
import numpy

N = int(input("Количество элементов в массиве"))
A = [random.randint(-1, 1) for i in range(0, N)]

print(A)

for i in range(N):
    if A[i] == 0 and A[i-1] == 0:
        print("Два подряд нуля в ",i-1,"и",i)
