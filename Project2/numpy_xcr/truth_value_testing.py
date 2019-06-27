import numpy as np


def count_rows_with(n,m):
    return np.sum(np.any(m == n, axis=1))


def is_monotonically_increasing(arr):
    return np.diff(arr) > 0

