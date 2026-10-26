sample = [90, 80, 63, 87]
weights = [0.2, 0.2, 0.2, 0.4]
answer = []
for key, value in zip(sample, weights):
    answer.append(key * value)

weighted_mean = sum(answer) / sum(weights)
print(weighted_mean)