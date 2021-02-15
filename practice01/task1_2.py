from math import log as ln, pow, sin

from helpers import exp_cast

# Задача 1.2
def f12(x):
    if x < 45:
        return exp_cast(ln(abs(sin(x))) + 56 * x)
    if x >= 91:
        return exp_cast(pow(x, 6) - pow(x, 4))
    return exp_cast(7 * pow((x - 17 * pow(x, 4)), 3) + sin(x))

print(f12(129))
print(f12(-28))
