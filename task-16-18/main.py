#!/bin/python
import random
num_list = [random.randint(0, 9) for _ in range(int(input("Введите количество элементов: ")))]
print(num_list)
x = int(input("Введите искомое число: "))
min_dist = abs(x - num_list[0])
min_item = num_list[0]
count = 0
for i in num_list:
    dist = abs(x - i)
    if dist < min_dist:
        min_dist = dist
        min_item = i
    if dist == 0:
        count += 1
if count > 0:
    print(f"Число {x} встретилось {count} раз.")
else:
    print(f"Число {x} не встретилось. Ближайшее число - {min_item}.")
