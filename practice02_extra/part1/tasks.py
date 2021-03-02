from practice02_extra.constants import *
import sys
import random

def conv_to_int(s):
    """
    Преобразование элементов списка s из строковой в числовую форму.
    :param s: Исходный список со строковымии числами.
    :return: Список с числами типа int.
    """
    return [int(i) for i in s]

def distinct_el_num(s):
    """
    Подсчёт количества различных элементов в последовательности s.
    :param s: Исходная последовательность.
    :return: Число уникальных значений.
    """
    return len(set(s))

def reverse_list(s):
    """
    Обращение последовательности s без использования функций.
    :param s: Исходная последовательность.
    :return: Обращённая последовательность.
    """
    return s[::-1]

def find_idx(x, s):
    """
    Выдача списка индексов, на которых найден элемент x в последовательности s.
    :param x: Элемент, индексы которого необходимо найти.
    :param s: Исходная последовательность.
    :return: Список индексов.
    """
    return [i for i in range(len(s)) if x == s[i]]

def sum_on_even_idx(s):
    """
    Сложение элементов списка s с чётными индексами.
    :param s: Исходный список.
    :return: Сумма элементов, находящиихся на чётных индексах.
    """
    return sum(s[::2])

def find_longest_str(s):
    """
    Поиск строки максимальной длины в списке строк s.
    :param s: Исходный список.
    :return: Самая длинная строка в списке.
    """
    return max(s, key=len)

def shorter():
    """
    Сократите код до 19 символов без использования функций.
    return ["much", "code", "wow"][i] # 24 символа
    :return: Первый элемент списка.
    """
    i = 0
    return "muchcodewow"[:i + 4]  # 19 символов

def generate_groups(group_str):
    """
    Напишите генерацию всех названий групп в том виде, в котором используется
    в выпадающем списке на сайте с результатами от робота kispython.
    :param group_str: Название группы.
    :return: Преобразованное название группы.
    """
    return "{0}{1}".format(group_str[1], int(group_str[5:7]))

def zip_work():
    """
    Изучите, как работает функция zip().
    :return: Список из кортежей, содержащих пары по позициям.
    """
    a = [77, 44, 5]
    b = [3.5, 0.0, -1.0]
    c = ["java", "python", "kotlin"]
    zipped = zip(a, b, c)
    return list(zipped)

def mul_digits(*digits):
    """
    Разберите роль операции * в создании функций с переменным числом
    аргументов, а также для распаковки последовательностей.
    :param digits: Переменное число входных параметров (чисел).
    :return: Произведение чисел.
    """
    res = 1
    for d in digits:
        res *= d
    return res

def transpose(matrix):
    """
    Реализуйте с помощью zip() функцию transpose() для транспонирования матрицы.
    :param matrix: Исходная матриица.
    :return: Транспонированная матрица.
    """
    return list(list(i) for i in zip(*matrix))

def digital_economy_report_generator():
    """
    Реализуйте генератор докладов по цифровой экономике.
    :return: Сгенерированный доклад
    """
    return " ".join(random.choice(i) for i in economy_data)

def my_print(*args, sep=" ", end="\n"):
    """
    Реализуйте свою версию print(). Постарайтесь использовать максимум
    возможностей настоящей print(). Для вывода используйте функцию
    sys.stdout.write().
    :param args: Аргументы для вывода.
    :param sep: Разделитель данных для вывода.
    :param end: Последний символ строки вывода.
    :return: Ничего не возвращает. Происходит вывод.
    """
    sys.stdout.write(sep.join(str(i) for i in args) + end)

def only_named_args(**args):
    """
    Реализуйте функцию, которая принимает только именованные аргументы. При
    передаче позиционного аргумента Питон должен выдать ошибку.
    :param args: Исходные аргументы
    :return: Словарь из ключей и значений.
    """
    return args

def generate_array(*dim):
    """
    Напишите функцию generate_array(dim1, dim2, dim3, ...) для создания
    многомерного массива с помощью вложенных списков.
    :param dim: Исходная последовательность аргументов.
    :return: Многомерный массив.
    """
    return [*dim]
