import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(lst).reshape(3, 3)

    calculations = {
        'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), float(matrix.mean())],
        'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)), float(matrix.var())],
        'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), float(matrix.std())],
        'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), float(matrix.max())],
        'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), float(matrix.min())],
        'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), float(matrix.sum())]
    }

    return calculations
