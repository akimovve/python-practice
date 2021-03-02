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

def test():
    # Задача 1
    assert conv_to_int(["2", "13", "1", "0"]) == [2, 13, 1, 0]
    # Задача 2
    assert distinct_el_num(["python", "hello", "world", "python"]) == 3
    # Задача 3
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    # Задача 4
    assert find_idx(4, [0, 4, 1, 4, 4, 2, 4]) == [1, 3, 4, 6]
    # Задача 5
    assert sum_on_even_idx([2, -1, -7, 4, 2, 8, 9, 1]) == 6
    # Задача 6
    assert find_longest_str(["java", "python", "c++", "sql"]) == "python"
    # Задача про 24 символа
    assert shorter() == "much"
    # Задача про генерацию названий групп
    assert generate_groups("ИКБО-01-19") == "К1"

    print("All tests passed")

test()
