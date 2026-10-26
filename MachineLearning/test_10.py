from sympy import *

n = symbols("n")
f = (1 + (1 / n)) ** n
result = limit(f, n, oo)
print(result)
print(result.evalf())