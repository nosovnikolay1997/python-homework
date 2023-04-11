#!/bin/python
inp = input("Введите номер билета с шестью цифрами: ")
if len(inp) == 6:
    sum1 = int(inp[0]) + int(inp[1]) + int(inp[2])
    sum2 = int(inp[3]) + int(inp[4]) + int(inp[5])
    if sum1 == sum2:
        print("yes")
    else:
        print("no")
else:
    print("Должно быть шесть цифр")
