from scipy.stats import norm

mean = 18
std_dev = 1.5

x = norm.cdf(21, mean, std_dev) - norm.cdf(15, mean, std_dev)
print(x)