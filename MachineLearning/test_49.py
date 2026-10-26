import numpy as np

basis = np.array(
    [[3, 0],
     [0, 2]]
)
v = np.array([1, 1])

new_v = basis.dot(v)

print(new_v)