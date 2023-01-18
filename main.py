# lambda. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.           Пример  [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]  -> [2, 4, 5, 9]
# from random import randint
# in_lst = []
# for i in range(11):
#     in_lst.append(randint(0,10))
# in_lst = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 8, 9, 10]
# print(in_lst)
# b = filter(lambda i : in_lst.count(i) < 2, in_lst)
# print(list(b))

# filter. Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
# b= filter(str.isalpha, a)
# c= filter(str.isdigit, a)
# print(*b)
# print(*c)

# map. Программа создает список и возводит все его значения в квадрат
# from random import randint
# numbers = []
# for i in range(10):
#     numbers.append(randint(0, 10))
# print(f'Cлучайный список: {numbers}')
# squared = map(lambda num: num ** 2, numbers)
# print(list(squared))

# zip. Программа группирует значения  нескольких обьектов по их индексам
# name = "Александр", "Иван", "Людмила", "Елена"
# id = (32, 43, 25, 38)
# salary = (2443, 5243, 3214, 100)
# print(list(zip(name, id, salary)))

# enumerate. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# N = int(input("Введите N: "))
# my_list = [int(i) for i in range(N + 1)]
# f = lambda x: 3 * x + 1
# for i in range(len(my_list)):
#     my_list[i] = f(my_list[i])
# my_list.remove(my_list[0])
# print(dict(enumerate(my_list, 1)))

# list comprehension. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:*  6782 -> 23   0,56 -> 11
# def sum(n):
#     sum = 0
#     for i in n:
#         if i != '.':
#             sum = sum + int(i)
#     return sum
# n = input('Введите любое вещественное число: ')
# print(f'Сумма цифр в числе равна {sum(n)}')
# Вариант с использованием list comprehension
# n = input("Введите любое вещественное число: ")
# summa = sum([int(digit) for digit in n if digit.isdigit()])
# print(summa)

