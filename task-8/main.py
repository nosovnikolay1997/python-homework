#!/bin/python
n = int(input("Введите длину шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Введите количество долек: "))
if (k%n == 0 and k//n <= m) or (k%m == 0 and k//m <= n):
    print("yes")
else:
    print("no")
