from sympy import *

x, i, n = symbols("x i n")
f = x ** 2 + 1
lower, upper = 0, 1
delta_x = (upper - lower) / n
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()
area = limit(n_rectangles, n , oo)

print(area)