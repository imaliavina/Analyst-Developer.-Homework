'''
30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби.

*Сохранить словарь в файл users_hobby.txt.

Фрагмент файла с данными о пользователях (users.txt):
Иванов Иван Иванович
Петров Петр Петрович
Фрагмент файла с данными о хобби (hobby.txt):
скалолазание, охота
горные лыжи
'''

with open('users.txt', 'w', encoding='Utf-8') as f:

    users = ['Иванов Иван Иванович', 'Петров Петр Петрович', 'Сидоров Иван Сидорович',
              'Шариков Петр Алексеевич', 'Перепелкин Алексей Иванович']

    for user in users:
        f.write(user + '\n')

with open('hobby.txt', 'w', encoding='Utf-8') as f:
    hobbies = ['Скалолазание, охота', 'Горные лыжи', 'Фотография',
             'Бисероплетение', 'Книги, танцы']

    for hobby in hobbies:
        f.write(hobby + '\n')

users_hobby = {}

with open('users.txt', 'r', encoding='Utf-8') as f1:
    with open('hobby.txt', 'r', encoding='Utf-8') as f2:

        while user:
            user = f1.readline()[:-1]
            hobby = f2.readline()[:-1]
            users_hobby[user] = hobby

            if not user:
                del users_hobby['']

with open('users_hobby.txt', 'w', encoding='Utf-8') as f:
    for key, value in users_hobby.items():
        f.write(f'{key} : {value}' + '\n')


'''
31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''


def simple_product(n):

    prod_lst = []
    n_rest = n                 #то, что остается от n после деления на простой множитель

    for k in range(2, n):

        while n_rest % k == 0:
            prod_lst.append(k)
            n_rest /= k

    if len(prod_lst) == 0:
        print('Число простое')
        return [1, n]
    else:
        return prod_lst


num = int(input('Введите натуральное число:'))
print(f'Список простых множителей: {simple_product(num)}')


'''
32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
элементов исходной последовательности.
'''

seq = map(int, input('Введите последовательность чиcел через пробел:').split())

just_once = []

for k in seq:
    if k not in just_once:
        just_once.append(k)

print(just_once)


'''
33. *Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
'''

from random import randint


def write_polynom(coef_lst, file_name):

    k = len(coef_lst) - 1

    with open(file_name, 'w') as f:

        for i in range(k+1):
            if i == k:
                f.write(f'{coef_lst[i]} = 0')
            else:
                f.write(f'{coef_lst[i]} x^{k - i} + ')


k = int(input('Введите степень многочлена k:'))
coef_lst = [randint(0, 100) for i in range(k + 1)]  #создаем случайные коэф-ты
print(f'Коэффициенты: {coef_lst}')
write_polynom(coef_lst, 'file.txt')


'''
34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
содержащий сумму многочленов.
2x² + 4x + 5 = 0  и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0 
'''

#Записываем в файл с помощью фуекции из предыдущего задания write_polynom:

write_polynom([1, 2, 3, 4], 'file1.txt')
write_polynom([4, 5, 6, 3, 1], 'file2.txt')

# Функция, которая считывает из файла коэффициенты многочлена:


def read_polynom(file_name):

    with open(file_name, 'r') as f:

        s = f.read()
        s_lst = s[:-3].split('+')           #работа со строкой, полученной из файла. Разделяем по "+", переводим в список
        #print(s_lst)

        new_lst = []

        for each in s_lst:
            if 'x' in each:
                x_pos = each.index('x')                #ищем позицию "x", чтобы удалить из строки и оставить только числа
                new_lst.append(int(each[:x_pos]))
            else:
                new_lst.append(int(each))

        print(new_lst)

    return new_lst


coef_lst1 = read_polynom('file1.txt')      #считываем из файла
coef_lst2 = read_polynom('file2.txt')

write_polynom(coef_lst1, 'file3.txt')      #записываем в новый файл
write_polynom(coef_lst2, 'file4.txt')