#!/bin/python
import random
min_limit = 0
max_limit = 10
list1 = [random.randint(min_limit, max_limit) for _ in range(int(input("Введите количество элементов первого множества: ")))]
print(list1)
list2 = [random.randint(min_limit, max_limit) for _ in range(int(input("Введите количество элементов второго множества: ")))]
print(list2)
print(set(list1).intersection(set(list2)))
