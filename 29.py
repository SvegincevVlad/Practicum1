"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 1.py
Автор: 2020 © В.С. Свежинцев, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/12/2020
Дата последней модификации: 11/12/2020
Связанные файлы/пакеты: numpy, random
Описание:Известен ГОД. Определить, будет ли этот год високосным, и к какому веку этот год относится.
#версия Python: 3.9.0
"""
X = int(input("Введите год для проверки:"))

if (X % 4 == 0 and X % 100 != 0) or (X % 400 == 0):
    print("Год невисокосный:")
else:
    print("Год високосный")
if X % 100 == 0:
    X = X // 100
    print(X," век")
elif X % 100 != 0:
    X = (X // 100) + 1
    print(X," век")
