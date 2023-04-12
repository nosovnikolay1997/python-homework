#!/bin/python
import random
amount = int(input("Введите количество монеток: "))
count0 = 0
count1 = 0
for i in range(amount):
    current = random.randint(0, 1)
    print(current, end=' ')
    if current == 0:
        count0 += 1
    else:
        count1 += 1
print()
if count0 < count1:
    print(count0)
else:
    print(count1)
