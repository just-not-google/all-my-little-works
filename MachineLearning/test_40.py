import math
from sympy import integrate

def normal_pdf(x: float, mean: float, str_dev: float) -> float:
    return (1.0 / (2.0 * math.pi * str_dev ** 2) ** 0.5) * math.exp(-1.0 * ((x - mean) ** 2 / (2.0 * str_dev ** 2)))

def integral_normal_pdf(x: float, mean: float, str_dev: float):
    return integrate(normal_pdf(x, mean, str_dev), x)

print(integral_normal_pdf(1, 64.43, 2.99))

