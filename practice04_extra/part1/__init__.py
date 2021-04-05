from Person import Person
from practice04_extra.part1.expression_trees.models.Add import Add
from practice04_extra.part1.expression_trees.models.Mul import Mul
from practice04_extra.part1.expression_trees.models.Num import Num
from practice04_extra.part1.expression_trees.visitors.CalcVisitor import \
    CalcVisitor
from practice04_extra.part1.expression_trees.visitors.PrintVisitor import \
    PrintVisitor
from practice04_extra.part1.expression_trees.visitors.StackVisitor import \
    StackVisitor

from practice04_extra.part1.hash_table.HashTable import HashTable
from practice04_extra.part1.html.Html import Html


def test_hash_table():
    """
    Реализуйте свою структуру данных, хэш-таблицу, аналог встроенного dict.
    Используйте функцию hash. Примените тестирование на случайных данных.
    1. Реализуйте методы чтения, записи, получения размера хэш-таблицы.
    2. Сделайте вышеупомянутые методы стандартными операторами/функциями,
    по аналогии с dict.
    3. Реализуйте поддержку для цикла for.
    :return:
    """
    print('Task with hash table')
    table = HashTable()

    for i in range(5000):
        table[i] = i + 1
        assert table[i] == i + 1
        assert table[chr(i)] is None

    assert len(table) == 5000

    for key, value in table:
        print(str(key) + ': ' + str(value))


def task1():
    """
    Напишите код, который выведет на экране все переменные объекта
    произвольного пользовательского класса.
    :return:
    """
    print('\nTask 1')
    p1 = Person('Martin', 'Green', 20)
    print(dir(p1))
    print(vars(p1))
    print(p1.__dict__)


def task2():
    """
    Напишите код, который по имени метода, заданному строкой, вызовет этот
    метод в некотором пользовательском классе.
    :return:
    """
    print('\nTask 2')
    p1 = Person('Martin', 'Green', 20)
    method_to_invoke = getattr(p1, 'get_info')
    print(method_to_invoke())


def task3():
    """
    Работа с деревьями выражений
    1. Реализовать классы Num, Add, Mul.
    2. Реализовать класс-посетитель PrintVisitor для печати выражения.
    Обойтись без операторов ветвления.
    3. Реализовать класс-посетитель CalcVisitor для вычисления выражения.
    Обойтись без операторов ветвления.
    4. Реализовать класс-посетитель StackVisitor для порождения кода стековой
    машины по выражению. Обойтись без операторов ветвления.
    5. Добавьте классы Sub и Mul. В существующий код можно только добавлять
    новые строки, не изменяя старой части.
    :return:
    """
    print('\nTask 3')
    ast = Add(Num(7), Mul(Num(3), Num(2)))
    pv = PrintVisitor()
    cv = CalcVisitor()
    sv = StackVisitor()
    print(pv.visit(ast))
    print(cv.visit(ast))
    sv.visit(ast)


def test_html():
    """
    Язык HTML-тегов с помощью менеджера контекста.
    Реализовать классы для выполнения примера.
    :return:
    """
    print('\nTask with html object')
    html = Html()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')
    print(html.data)


if __name__ == '__main__':
    test_hash_table()
    task1()
    task2()
    task3()
    test_html()
