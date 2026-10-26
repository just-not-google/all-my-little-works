from scipy.stats import norm

x = norm.ppf(0.95, loc=64.43, scale=2.99)
print(x)