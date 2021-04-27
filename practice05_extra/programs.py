import re


def p5(hypertext: str) -> str:
    """
    Программа для тестирования 5.
    Транслятор, который удаляет HTML-теги и оставляет обычный текст
    """
    return re.sub('<[^>]*>', '', hypertext)


def sqrt_func(x: float, epsilon: float) -> float:
    """
    Программа для тестирования 6.
    Square Root
    Newton-Raphson method implementation.
    """
    approx = x / 2
    while abs(x - approx) > epsilon:
        approx = 0.5 * (approx + x / approx)
    return approx
