from math import e, pow, sin, sqrt, tan

from helpers import exp_cast

# Задача 1.1
def f11(x):
    res = sqrt(abs(x) - sin(x) - 1) - (pow(x, 5) - tan(x) + 2) - sqrt(
            (94 * pow(x, 4) - pow(e, x) / (54 * pow(x, 5) - pow(x, 8))))
    return exp_cast(res)

print(f11(52))
print(f11(51))
