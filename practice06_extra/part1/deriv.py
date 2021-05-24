import sympy as sy


def deriv(func):
    x = sy.Symbol('x')

    def take(x):
        return sy.diff(func(x), x)

    def substitution(dig):
        return take(x).subs(x, dig)

    return substitution
