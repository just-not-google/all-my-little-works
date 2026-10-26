from sympy import *

x, s = symbols("x s")
f = x ** 2
slope_f = (f.subs(x, x + s) - f) / ((x + s) - x)
slope_2 = slope_f.subs(x, 2)
result = limit(slope_2, s, 0)
print(result)