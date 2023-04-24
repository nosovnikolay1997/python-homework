#!/bin/python
import random
min_limit = 0
max_limit = 10
n = int(input("Введите количество кустов на грядке: "))
first = prevprev = random.randint(min_limit, max_limit)
second = prev = random.randint(min_limit, max_limit)
current = random.randint(min_limit, max_limit)
res = prevprev + prev + current
print(f"{prevprev} {prev} {current}", end=' ')
for _ in range(n-3):
    prevprev = prev
    prev = current
    current = random.randint(min_limit, max_limit)
    print(current, end=' ')
    if (prevprev + prev + current > res):
        res = prevprev + prev + current
if prev + current + first > res:
    res = prev + current + first
if current + first + second > res:
    res = current + first + second
print(f"\n{res}")
