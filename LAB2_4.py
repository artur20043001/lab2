import csv
from colorama import init
from colorama import Back
init(autoreset=True)
c=0
c1=0
c2=0
with open('books.csv', "r") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table):
        if c>0:
            if int(row[6][:4])>=2015:
                c1+=1
            else:
                c2+=1
        c+=1
print(c1/(c1+c2),c2/(c1+c2))
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   ')
print(Back.BLACK + '   '+Back.LIGHTWHITE_EX + '    '+Back.BLACK + '   ')
print(Back.BLACK + '   '+Back.LIGHTWHITE_EX + '    '+Back.BLACK + '   ')
print(Back.BLACK + '   '+Back.LIGHTWHITE_EX + '    '+Back.BLACK + '   ')
print(Back.BLACK + '   '+Back.LIGHTWHITE_EX + '    '+Back.BLACK + '   ')