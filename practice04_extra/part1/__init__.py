from Person import Person
from practice04_extra.part1.expression_trees.Add import Add
from practice04_extra.part1.expression_trees.Mul import Mul
from practice04_extra.part1.expression_trees.Num import Num
from practice04_extra.part1.expression_trees.PrintVisitor import PrintVisitor


def task1():
    """
    Напишите код, который выведет на экране все переменные объекта
    произвольного пользовательского класса.
    :return:
    """
    print('Task 1')
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
    print('\nTask 3')
    ast = Add(Num(7), Mul(Num(3), Num(2)))
    pv = PrintVisitor()
    print(pv.visit(ast))


if __name__ == '__main__':
    task1()
    task2()
    task3()
