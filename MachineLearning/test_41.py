def z_score(x, mean, std):
    return (x - mean) / std

def z_to_x(z, mean, std):
    return (z * std) + mean

mean = 140000
std_dev = 3000
x = 150000

z = z_score(x, mean, std_dev)
back_to_x = z_to_x(z, mean, std_dev)

print(z)
print(back_to_x)