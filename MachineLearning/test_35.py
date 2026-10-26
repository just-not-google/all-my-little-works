from math import sqrt

data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / len(values)
    return _variance

def str_dev(values):
    return sqrt(variance(values))

print(str_dev(data))