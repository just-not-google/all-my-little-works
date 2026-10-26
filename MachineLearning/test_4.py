from sympy import  *

x = symbols("x")
expr = x ** 2 / x ** 5
expr_1 = expr * x ** 3
print(expr_1)