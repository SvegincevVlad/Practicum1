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
M=random.randint(1,4)
arr=[random.randint(1,10) for i in  range(M)]
m=0
for i in range (M):
    arr[i]=input()
    for i in renge(M):
        m=0
        for n in range(len(arr([i])))
                 S=arr[i]
                 if S[n]=="a" or  S[n]== "е" or S[n]=="ё" or S[n]=="и" or s[n]=="о"
                 or S[n]=="ю"  or S[n]=="э" or S[n]=="ы" or S[n]=="у" or S[n]=="я":
                     m+=1
    print("Количество гласных букв в слове"+"\"" +str(arr[i])+"\"" + "равно"+str(m))
