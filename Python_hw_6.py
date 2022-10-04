'''
32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
элементов исходной последовательности.
'''

seq = map(int, input('Введите последовательность чиcел через пробел:').split())

dict = {}

for s in seq:
    if s not in dict.keys():
        dict[s] = 1
    else:
        dict[s] += 1

print(dict)

print(list(filter(lambda i: dict[i] == 1, dict)))

'''
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)  
'''

import math

n = int(input('Введите число:'))

print(list(map(lambda b: math.factorial(b), list(range(1, n+1)))))

'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле
# file.txt в одной строке одно число.
'''

import random
import math
import numpy as np

n = int(input('Введите число n:'))

n_lst = [random.randint(-n, n) for i in range(n)]
print(f'Исходный список: {n_lst}')

#---Ввод позиций с клавиатуры---------------------------------

while True:
    pos = input('Введите позиции для перемножения элементов:').split()
    pos = [int(p) if int(p) < n else -1 for p in pos]
    print(f'Выбранные позиции: {pos}')
    if -1 not in pos:
        break
    else:
        print('Неправильно выбраны позиции.')


need_values = [value for i, value in enumerate(n_lst) if i in pos]
print(f'Элементы на выбранных позициях: {need_values}')
#print(math.prod(need_values, 0))

print(np.prod(need_values))

'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11
'''

num = input('Введите вещественное число:')
num_lst = list('1234567890')
summa = 0

print(sum(list(map(int, list(filter(lambda s: s in num_lst, num))))))

'''
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

import math

x1, y1 = map(int, input('Введите координаты первой точки через пробел:').split())
x2, y2 = map(int, input('Введите координаты второой точки через пробел:').split())

s = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'Расстояние между точками: {round(s, 2)}')




