from scipy.stats import beta

a = 30
b = 6
p = 1.0 - beta.cdf(0.90, a, b)
print(p)