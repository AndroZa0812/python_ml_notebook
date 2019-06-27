import numpy as np


def check_sudoku(sud):
    return


sudoku = """145327698
            839654127
            672918543
            496185372
            218473956
            753296481
            367542819
            984761235
            521839764"""
grid = np.array([[int(i) for i in line] for line in sudoku.split()])

if check_sudoku(grid):
    print("Grid Valid")
else:
    print("Grid invalid")
