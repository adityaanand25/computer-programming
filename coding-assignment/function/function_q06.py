# A student is trying to find the roots of a quadratic equation but is encountering errors. Help him fix his code.

from math import sqrt
def quad(b, c, a=1):
    x = b * b - 4 * a * c
    if x < 0:
        return "Sorry, complex root(s)"
    d = sqrt(x)
    r1 = (-b + d) / (2 * a)
    r2 = (-b - d) / (2 * a)
    return r1, r2
print(quad(1, 1, 2))
print(quad(3))
print(quad(2, 1))
