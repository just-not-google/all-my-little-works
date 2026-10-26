from scipy.stats import norm

mean = 64.43
str_dev = 2.99
x = norm.cdf(64.43, mean, str_dev)
print(x)