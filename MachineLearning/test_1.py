from sympy import *
from sympy.plotting import plot3d

def f_1(x: int) -> int:
    return x ** 2

def f_2(y: int) -> float:
    return y / 2

x, y = symbols("x y")
f = 2 * f_1(x) + 3 * f_2(y)
plot3d(f)

