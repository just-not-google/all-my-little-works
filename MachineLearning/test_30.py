from scipy.stats import beta

a = 8
b = 2
p = beta.cdf(0.90, a, b) - beta.cdf(0.80, a, b)
print(p)