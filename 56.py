"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 1.py
Автор: 2020 © В.С. Свежинцев, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 18/12/2020
Дата последней модификации: 18/12/2020
Связанные файлы/пакеты: numpy, random
Описание:
#версия Python: 3.9.0
"""
import random
M=random.randint(1,4)
arr=[random.randint(1,10) for i in range(M)]
for i in range (M):
    arr[i]=input()
    print(arr)
    for i in range (M):
        if len(arr[i])%2==1:
            S=arr[i]
            print(S[len(arr[i])//2])
