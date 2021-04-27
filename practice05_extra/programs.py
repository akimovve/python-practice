import re


def p1(a, b, c):
    """
    Программа для тестирования 1.
    Установление по сторонам (a, b, c) треугольника его типа:
    равносторонний, разносторонний, равнобедренный.
    """
    if a == b == c:
        return 'равносторонний'
    if a == b or a == c or b == c:
        return 'равнобедренный'
    return 'разносторонний'


def p2(password):
    """
    Программа для тестирования 2.
    Функция проверки пароля на безопасность (например: безопасный пароль
    содержит комбинирование шести или больше строчных и прописных букв,
    плюс знаки препинания и цифры).
    """
    return re.match(
        r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[.,;!?]).{6,}$',
        password)


def p3(ipv4):
    """
    Программа для тестирования 3.
    Проверка IPv4-адреса на корректность.
    """
    return re.match(
        r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b',
        ipv4)


def p5(hypertext):
    """
    Программа для тестирования 4.
    Транслятор, который удаляет HTML-теги и оставляет обычный текст
    """
    return re.sub('<[^>]*>', '', hypertext)


def sqrt(x, epsilon):
    """
    Программа для тестирования 5.
    Square Root
    Newton-Raphson method implementation.
    Input:
        x: A float
        epsilon: A float
    Precondition:
        x >= 1 and epsilon > 0
    Output:
        A float in the interval [sqrt(x) - epsilon, sqrt(x) + epsilon]
    Example:
        >>> sqrt(2, 0.01)
        1.4166666666666665
    """
    approx = x / 2
    while abs(x - approx) > epsilon:
        approx = 0.5 * (approx + x / approx)
    return approx
