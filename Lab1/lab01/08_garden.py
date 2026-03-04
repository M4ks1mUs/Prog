#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = []
for i in garden:
    if garden_set.count(i) == 0:
        garden_set.append(i)

meadow_set = []
for i in meadow:
    if meadow_set.count(i) == 0:
        meadow_set.append(i)

print(garden_set)
print(meadow_set)

# выведите на консоль все виды цветов
# TODO здесь ваш код
for i in garden_set:
    print(i, end = " ")

for i in meadow_set:
    if garden_set.count(i) == 0:
        print(i, end = " ")

print()

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
for i in garden_set:
    if meadow_set.count(i) == 1:
        print(i, end = " ")

print()

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
for i in garden_set:
    if meadow_set.count(i) == 0:
        print(i, end = " ")

print()

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
for i in meadow_set:
    if garden_set.count(i) == 0:
        print(i, end = " ")

print()
