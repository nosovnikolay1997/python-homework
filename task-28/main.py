#!/bin/python
def dec(a):
    return a - 1

def inc(a):
    return a + 1

def sum(a, b):
    if b == 0:
        return a
    return inc(sum(a, dec(b)))

print(sum(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
