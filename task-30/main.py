#!/bin/python
a0 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
print([a0 + i * d for i in range(int(input("Введите количество элементов: ")))])
