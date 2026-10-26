from scipy.stats import norm

mean = 64.43
str_dev = 2.99

x = norm.cdf(66, mean, str_dev) - norm.cdf(62, mean, str_dev)

print(x)