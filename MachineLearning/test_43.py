import random
import plotly.express as px

answer = []
for _ in range(10000):
    lst = [random.randint(1, 6) for _ in range(5)]
    answer_1 = sum(lst) / len(lst)
    answer.append(answer_1)

px.histogram(x=answer).show()
