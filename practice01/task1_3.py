from math import sin, tan

from helpers import exp_cast

# Задача 1.3
def f13(n, m):
    res = 0
    for i in range(1, n + 1):
        res += abs(i) - sin(i) - 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res += i - tan(j) + 2
    return exp_cast(res)

print(f13(58, 88))
print(f13(78, 35))
