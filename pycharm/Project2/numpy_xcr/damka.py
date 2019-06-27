import numpy as np

m = np.ones((8, 8))
m[::2, ::2] = 0
m[1::2, 1::2] = 0
print(m)
