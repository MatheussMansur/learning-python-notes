import math

import numpy as np

print(math.pow(2, 5))
print(math.ceil(3.45), math.floor(5.25))
print(math.fabs(-10.33))
print(round(math.log(1000, 10), 2))

# list vs numpy array
print([1, 2, 3] * 3)
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
print(u * 3)
print(u + v)
print(u * v)
print(np.dot(u, v))

# dot product by hand to check
total = 0
for i in range(len(u)):
    total += u[i] * v[i]
print(total == np.dot(u, v))
