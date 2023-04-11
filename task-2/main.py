#!/bin/python
inp = int(input("Введите трёхзначное число: "))
if inp < 100 or inp > 999:
    print("Число должно быть трёхзначное!")
else:
    res = inp % 10
    inp //= 10
    res += inp % 10
    inp //= 10
    res += inp
    print(f"Сумма цифр: {res}")
