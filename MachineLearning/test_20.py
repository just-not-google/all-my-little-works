from sympy import *
from sympy.plotting import plot

x= symbols("x")
f = x ** 2 + 1
area = integrate(f, (x, 0, 1))
print(area)
plot(f)