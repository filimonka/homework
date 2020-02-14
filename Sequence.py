import random
from functools import reduce


def name_list(a, b): # Новый список имён
    new_list = a * b
    return random.sample(new_list, k=n)


def freq_name(names): # Самое частое имя
    my_dict = {}
    for el in names:
        if el not in my_dict:
            my_dict[el] = 1
        else:
            my_dict[el] += 1
    a = list(my_dict.items())
    a.sort(key=lambda x: x[1], reverse=True)
    return a[0][0]


def rare(l): # Самая редкая буква
    new_dict = {}
    for el in l:
        if el[0] not in new_dict:
            new_dict[el[0]] = 1
        else:
            new_dict[el[0]] += 1
    a = list(new_dict.items())
    a = reduce(lambda x, y: x if x < y else y, a)
    return a[0]


name = ["ann", "peter", "mark", "kate", "murka", "pashtet", "ben","vasya", "yana", 'lena',
        'sasha', 'polya', 'polya', 'tanya', 'olya', 'masha', 'snejka', 'varya', 'yura', 'kolya', 'slava']
n = 100


# Лог. Сделала возможно не правильно, но у меня работает...


def compare(x, y):
    if x[0] > y[0]:
        return x
    elif x[0] == y[0]:
        if x[1] > y[1]:
            return x
        else:
            return y
    else:
        return y


file = open("log (1)", 'r', encoding='utf-8')
lines = file.readlines()
time_list = []
for line in lines:
    time_list.append(line.split(" - "))
result = reduce(lambda x, y: compare(x, y), time_list)
print(result)
