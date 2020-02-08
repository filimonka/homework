# Задача 1

'''
for i in range(1,6):
    print(i, "000000000000000000000000000000000000")
'''

# Задача 2
'''
a = input('enter 10 figures')
five = 0
for i in a:
    if (int(i)) == 5:
        five += 1
print(five)
'''

#Задача 4
'''
mult = 1
for i in range(1,11):
    mult *= i
print(mult)
'''

#Задача 5
'''
number = int(input())
while number > 0:
    print(number % 10)
    number = number // 10
'''

#Задача 6
'''
number = int(input('Введите число'))
sum = 0
while number > 0:
    sum += number % 10
    number = number // 10
print(sum)
'''

#Задача 7
'''
number = int(input('Введите любое число больше 0'))
mult = 1
while number > 0:
    mult *= number % 10
    number = number // 10
print(mult)
'''

#Задача 9
'''
number = int(input('Введите число'))
max = 0
while number > 0:
    if number % 10 > max:
        max = number % 10
    number = number // 10
print(max)
'''

#Задача 10
'''
number = int(input('Введите любое число больше 0'))
i = 0
while number > 0:
    if number % 10 == 5:
        i += 1
    number = number // 10
print(i)
'''
