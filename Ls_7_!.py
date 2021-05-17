import random

"""
Создать функцию, которая на вход принимат неопределённое число аргументов,
и именованный параметр mean_type. В зависимости от mean_tupe вернуть среднее
арифмитическое или среднее геометриеское. Выполнить программу в виде 3 - х функций.
"""


def mean(*args, mean_type):
    if mean_type == 1:
        return mean_sum(*args)
    elif mean_type == 2:
        return mean_mult(*args)
    else:
        return print("Введены неверные данные!")


def mean_sum(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum / len(args)


def mean_mult(*args):
    mult = 1
    for i in range(len(args)):
        mult *= args[i]
    return mult ** (1 / len(args))


print(mean(1, 2, 3, 4, 5, mean_type=3))

exit()
"""
Создать функцию, которая на вход принимат неопределённое число именованных аргументов,
и выводит на экран те из них длинна ключей которых чётна
"""


def my_func_dict(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key, value)


my_func_dict(Минск=100, Борисов=5, Слуцк=73, Орша=26, Гомель=253)

exit()


def func_dict(**kwards):
    for key, value in kwards.items():
        print(key, value)


func_dict(a=5)

exit()
"""
Написать програму которая принимает неограниченное число параметров
и возвращает их сумму и максимальное из них число
"""


def func_sum(*args):
    res_sum = 0
    res_max = 0
    for i in range(len(args)):
        res_sum += args[i]
        if res_max < args[i]:
            res_max = args[i]
    return res_sum, res_max


s, m = func_sum(1, 2, 3, 4, 5)
print(s)
print(m)

exit()
"""
Написать функцию принимающую неопределённое количество параметров и возвращающую args*i
"""


def my_func(*args):
    result = 0
    for i in range(len(args)):
        result += args[i] * i
    return result


print(my_func(4, 3, 2, 1))
print(my_func(1, 2, 3))
print(my_func(5, 1, 0, 8))

exit()
"""
Реализовать функцию, которая возвращает матрицу, на вход принимает размерность,
random_a - 1, random_b - 9
"""


def matrix(n, random_a=1, random_b=9):
    matrix_n = []
    for i in range(n):
        lst = []
        for j in range(n):
            lst.append(random.randint(random_a, random_b))
        matrix_n.append(lst)
    return matrix_n


print(matrix(5))

exit()
"Программа подсчёта факториала"


# Способ 1

def factorial_func(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1
    print(result)


def factorial_func2(n):
    if n == 1:
        return 1

    else:
        return n * factorial_func2(n - 1)


factorial_func(5)
print(factorial_func2(3))
