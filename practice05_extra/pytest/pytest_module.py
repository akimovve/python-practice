import re

import pytest as pytest


class Program:
    def __init__(self, func):
        self.func = func

    def invoke(self, param):
        return self.func(param)


@pytest.fixture
def program_2():
    p = Program(p2)
    return p


@pytest.fixture
def program_3():
    p = Program(p3)
    return p


@pytest.mark.parametrize('prop,res', [
    (',?qwErT123', True),
    ('qwer,15', False),
    ('Qwer,15', True),
    ('Qw1?', False),
    ('123', False),
    ('', False)
])
def test_p2(program_2, prop, res):
    assert program_2.invoke(prop) is res


@pytest.mark.parametrize('prop,res', [
    ('0.0.0.1', True),
    ('172.16.254.1', True),
    ('255.255.255.255', True),
    ('127.127.256.127', False),
    ('12764.231.18', False),
    ('127.b.c.d', False),
    ('a.b.c.d', False),
    ('', False)
])
def test_p3(program_3, prop, res):
    assert program_3.invoke(prop) is res


def test_p2_input(monkeypatch):
    inputs = ['QWERTYuiop,?/0']

    def custom_input(x):
        return inputs.pop()

    monkeypatch.setattr('builtins.input', custom_input)
    assert p2_input() is True


# -------- Задачи -------- #
def p2(password: str) -> bool:
    """
    Программа для тестирования 2.
    Функция проверки пароля на безопасность (например: безопасный пароль
    содержит комбинирование шести или больше строчных и прописных букв,
    плюс знаки препинания и цифры).
    """
    return bool(re.match(
        r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[.,;!?]).{6,}$',
        password))


def p2_input() -> bool:
    """
    Программа для тестирования 2 (с вводом значения).
    Функция проверки пароля на безопасность (например: безопасный пароль
    содержит комбинирование шести или больше строчных и прописных букв,
    плюс знаки препинания и цифры).
    """
    x = input('Введите пароль:')
    return bool(re.match(
        r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[.,;!?]).{6,}$',
        x))


def p3(ipv4: str) -> bool:
    """
    Программа для тестирования 3.
    Проверка IPv4-адреса на корректность.
    """
    return bool(re.match(
        r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b',
        ipv4))
