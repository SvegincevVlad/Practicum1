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

N = int(input("Количество элементов массива"))
A = [1,5,3,-4]

print(A)

a = 0
for i in range(N):
    if A[i] >= 0:
        break
    if A[i] < 0:
        for i in range(N):
            if A[i-1] < A[i]:
                a = 0
            else:
                a =1
                break
        A[i] = A[i] - 1
        
if (a == 0):
    print("Возрастающая")
    
else:
    print("Убывающая")
