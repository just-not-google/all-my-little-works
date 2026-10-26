summation = sum(i * 2 for i in range(1, 6))
print(summation)

x = [1, 2, 3, 4]
n = len(x)
summation_1 = sum(10 * x[i] for i in range(0, n))
print(summation_1)

summation_2 = sum(10 * i for i in x)
print(summation_2)