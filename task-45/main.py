#!/bin/python
list1 = [sum([i for i in range(1, x) if x % i == 0]) for x in range(10000)]
print(set([(min(i, list1[i]), max(i, list1[i])) for i in range(len(list1)) if list1[i] < len(list1) and list1[list1[i]] == i != list1[i]]))
