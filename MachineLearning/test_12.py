from sympy import *

x = symbols("x")
f = x ** 3
dx_f = diff(f)
print(dx_f)