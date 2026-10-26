from sympy import *

i, n = symbols("i n")
summation = Sum(2 * i, (i, 1, n))
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit())