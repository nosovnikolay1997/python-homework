#!/bin/python
price = {}
for i in "aeioulnstrавеинорст":
    price.update({ i: 1})
for i in "dgдклмпу":
    price.update({ i: 2})
for i in "bcmpбгеья":
    price.update({ i: 3})
for i in "fhvwyиы":
    price.update({ i: 4})
for i in "kжзхцч":
    price.update({ i: 5})
for i in "jxшэю":
    price.update({ i: 8})
for i in "qzфщъ":
    price.update({ i: 10})
res = 0
for i in input("Введите слово: ").lower():
    res += price[i]
print(res)
