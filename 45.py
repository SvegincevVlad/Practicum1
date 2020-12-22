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
import numpy as np

N = int(input("Количество элементов массива"))
A = [random.randint(-10,10) for i in range(0,N)]
print(A)
Ao = []
Ap = []
for i in range(N):
    if A[i] > 0:
        Ap.append(A[i])
    if A[i] < 0:
        Ao.append(A[i])
sumAo = np.sum(Ao)
sumAp = np.sum(Ap)
sumAo = abs(sumAo)
Q = (sumAo-sumAp)

print(sumAo)
print(sumAp)
print(Q)

if sumAo == sumAp:
    print("Сумма отрицательных и положительных элементов массива равно")
if sumAo > sumAp:
    A.append([Q])
if sumAp > sumAo:
    A.append([Q])
    
print(A)
