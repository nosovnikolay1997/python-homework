#!/bin/python
print('Парам пам-пам' if len(set(map(len, ''.join(filter(lambda c: c.lower() in 'aeiouаоуыэяёеюи ', input("Введите строку: "))).split(' ')))) == 1 else 'Пам парам')
