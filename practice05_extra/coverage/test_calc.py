import random

import calc


def test_calc():
    for _ in range(10000):
        start(gen())


def start(s):
    try:
        return calc.calc(s)
    except:
        pass


def gen():
    a = '+-*/'
    b = '()'
    return ' '.join(
        [' '.join(
            [''.join(
                [str(random.choice(range(9)))
                 for _ in range(random.choice(range(1, 5)))]),
                random.choice(a), random.choice(b)])
            for _ in range(random.choice(range(5)))])
