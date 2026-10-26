def factorial(n: int):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

def binomial_coefficient(n: int, k: int, p: float):
    return factorial(n) / (factorial(k) * factorial(n - k))

def binomial_distribution(k: int, n: int, p: float):
    return binomial_coefficient(n, k) * (p ** k) * (1.0 - p) ** (n - k)

n = 10
p = 0.9

for k in range(n + 1):
    probability = binomial_coefficient(k, n, p)
    print(f"{k} - {probability}")