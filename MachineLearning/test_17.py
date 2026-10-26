from sympy import *
from sympy.plotting import plot

x = symbols("x")
z = (x ** 2 + 1) ** 3 - 2
dz_dx = diff(z, x)
print(dz_dx)
plot(z)
plot(dz_dx)
