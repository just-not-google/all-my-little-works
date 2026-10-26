sample = [1, 3, 2, 5, 7, 0, 2, 3]
keys = set(sample)
answer = dict()
for key in keys:
    answer[key] = 0
for i in sample:
    if i in answer:
        answer[i] += 1
maximum = max(answer.values())
final_answer = []
for key_1, value in answer.items():
    if value == maximum:
        final_answer.append(key_1)

print(final_answer)