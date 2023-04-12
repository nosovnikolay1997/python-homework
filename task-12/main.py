#!/bin/python
import math
sum_ = int(input("Введите сумму чисел: "))
product = int(input("Введите произведение чисел: "))
if product == 0:
    print(f"0 {sum_}")
else:
    d = sum_**2 - 4*product
    if d < 0:
        print("Решений нет.")
    else:
        y = (sum_ + int(math.sqrt(d)))//2
        x = product // y
        print(f"{y} {x}")
