import numpy as np
a = np.arange(1, 49).reshape(3, 4, 4)
"""task 1"""
print(a[:,1,:2])
"""task 2"""
print(a[2, 0,:1:-1])
"""task 3"""
print(a[:, ::-1,0])
"""task 4"""
print(a[:, ::-1, 0])
