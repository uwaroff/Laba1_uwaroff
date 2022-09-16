import csv
import random
a=0
b=0
with open('books.csv', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    for raw in list(table):
        b+=1
        if len(raw[1])>30:
            a+=1

    print(b-1)
    print(a)
    print('Введите желаемого автора')
    s = input()
with open('books.csv', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for raw in list(table):
        if raw[3] == s and int(raw[6][0:4:1]) >= 2018:
            print(raw)

e = 1
with open('books.csv', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    f = open("laba1.txt", 'w')
    for raw in list(table)[2:22]:
        f.write(str(e) +". " + raw[3] + ". " + raw[1] + " - " + raw[6][0:4:1] + "\n")
        e += 1

f.close()

