from math import pow

from helpers import exp_cast

# Задача 1.4
def count(n):
    if n == 0:
        return 2
    return 1 / 3 * count(n - 1) + 1 / 39 * pow(count(n - 1), 3)

def f14(n):
    return exp_cast(count(n))

print(f14(3))
print(f14(4))