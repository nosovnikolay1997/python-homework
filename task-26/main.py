#!/bin/python
def rec_power(a, b):
    if b == 0:
        return 1
    return a * rec_power(a, b-1)

print(rec_power(int(input("Введите основание степени: ")), int(input("Введите показатель степени: "))))
