"""
Задача 1.
Реализуйте функцию fast_mul в соответствии с алгоритмом двоичного умножения в
столбик. Добавьте автоматическое тестирование, как в случае с naive_mul.
"""

def fast_mul(x, y, res=0):
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return res + y
    if x % 2 != 0:
        res += y
    return fast_mul(x // 2, y * 2, res)

def test_fast_mul():
    for x in range(101):
        for y in range(101):
            assert fast_mul(x, y) == x * y
    print("All tests passed")

test_fast_mul()
