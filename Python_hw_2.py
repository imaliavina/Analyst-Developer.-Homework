# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите вещественное число:')
num_lst = list('1234567890')
summa = 0

for s in num:
    if s in num_lst:
        summa += int(s)

print(f'Cумма цифр {summa}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число:'))
multi = 1

for i in range(1, n+1):
    multi *= i

print(f'Произведение чисел равно: {multi}')

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число n:'))
summa = 0
seq = {}

for i in range(1, n+1):
    seq[i] = round((1+1/i)**i, 2)
    summa += seq[i]#

print(f'{seq} \nСумма последовательность для n={n}: {summa}')

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле
# file.txt в одной строке одно число.

import random

n = int(input('Введите число n:'))

n_lst = [random.randint(-n, n) for i in range(n)]
print(n_lst)

#---Ввод позиций с клавиатуры---------------------------------

while True:
    pos = input('Введите позиции для перемножения элементов:').split()
    pos = [int(p) if int(p) < n else -1 for p in pos]
    print(pos)
    if -1 not in pos:
        break
    else:
        print('Неправильно выбраны позиции.')

mul = 1
for p in pos:
    mul *= n_lst[p]

print(f'Произведение выбранных элементов: {mul}')

#---Ввод позиций из файла-------------------------------------

k = random.randint(2, n)    #количество элементов для перемножения
print(f'Количество элементов для перемножения {k}')

#запись в файл
with open('file', 'w') as f:
    for i in range(k):
        f.write(str(random.randint(0, n-1)) + '\n')

#чтение из файла
with open('file', 'r') as f:
    positions = f.readlines()
    positions = [int(s[0]) for s in positions]
    print(f'Позиции {positions}')

#перемножение элементов
mult = 1

for p in positions:
    mult *= n_lst[p]

print(f'Произведение элементов: {mult}')


#*Реализуйте алгоритм перемешивания списка.

import random

my_lst = ['1', '2', '3', '4', '5', '6', '7']
print(my_lst)

random.shuffle(my_lst)
print(my_lst)

#manual shuffle

for i in range(len(my_lst) - 1):
    k = random.randint(i+1, len(my_lst)-1)
    temp = my_lst[i]
    my_lst[i] = my_lst[k]
    my_lst[k] = temp

print(my_lst)























