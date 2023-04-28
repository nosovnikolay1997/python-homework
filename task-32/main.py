#!/bin/python
import random
gen_min = int(input("Введите минимальное значение при создании списка: "))
gen_max = int(input("Введите максимальное значение при создании списка: "))
list1 = [random.randint(gen_min, gen_max) for _ in range(int(input("Введите количество элементов списка: ")))]
print(list1)
filter_min = int(input("Введите минимальное значение при обходе списка: "))
filter_max = int(input("Введите максимальное значение при обходе списка: "))
print([i for i in range(len(list1)) if filter_min <= list1[i] <= filter_max])
