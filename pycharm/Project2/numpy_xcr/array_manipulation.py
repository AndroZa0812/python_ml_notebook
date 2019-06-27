import numpy as np

"""task 1"""
m = np.ones((3, 3))
"""task 2"""
m = np.vstack((m, [2, 2, 2]))
m = np.hstack((m, [[3], [3], [3], [3]]))
print(m)
