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
A = [A * 3 for A in 'abc']
print(A)
B = ['Hello', 'world!', 'qwe']
print(B)
list.sort(B, key=len)
print(B)

for i in range(len(B)):
    if len(B[i]) < len(B[i+1]):
        list.insert(0, '*')
        i = i + 1
        
print(B)
