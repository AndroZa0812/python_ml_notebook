import numpy as np


def get_saddle_points(mat):
    max_c = mat.max(axis=0)
    min_c = mat.min(axis=0)
    max_r = mat.max(axis=1)
    min_r = mat.min(axis=1)
    res_p1 = max_c[max_c == min_r]
    res_p2 = min_c[min_c == max_r]
    return np.append(res_p1, res_p2)


if __name__ == '__main__':
    mat = np.array([[10, 12, 7, 3, 12],
                    [3, 10, 6, 2, 8],
                    [18, 24, 17, 6, 10],
                    [15, 21, 10, 8, 12],
                    [1, 18, 22, 4, 15]])
    print(get_saddle_points(mat))
