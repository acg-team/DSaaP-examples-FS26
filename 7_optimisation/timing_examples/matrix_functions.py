
import numpy as np
import math as m

from helpers import report_performance

def do_math(value: float) -> float:
    """
    Performs some math on the given value.
    """
    return m.log((value / 2.0) + 1.0)


def do_math_row_column(matrix: list[list[float]]):
    """
    Applies the do_math function to each element of the given matrix in place,
    iterating row by row and column by column.
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0]) if n_rows > 0 else 0

    for i in range(n_rows):
        for j in range(n_cols):
            matrix[i][j] = \
                do_math(matrix[i][j])
    # 5000x5000 matrix: 3.0584232330322267 seconds


def do_numpy_math(value: np.float64) -> np.float64:
    """
    Performs some math on the given value using numpy.
    """
    return np.log((value / np.float64(2.0)) + np.float64(1.0))


def do_numpy_math_row_column(matrix: list[list[np.float64]]):
    """
    Applies the do_numpy_math function to each element of the given matrix in place,
    iterating row by row and column by column.
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0]) if n_rows > 0 else 0

    for i in range(n_rows):
        for j in range(n_cols):
            matrix[i][j] = do_numpy_math(matrix[i][j])
    # 5000x5000 matrix: 15.438082575798035 seconds


def divide_by_two_row_column(matrix: list[list[float]]):
    """
    Divides each element of the given matrix by 2 in place, iterating row by row and column by column.
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0]) if n_rows > 0 else 0

    for i in range(n_rows):
        for j in range(n_cols):
            matrix[i][j] /= 2.0
    # 5000x5000 matrix: 1.2901440143585206 seconds

def divide_by_two_column_row(matrix: list[list[float]]):
    """
    Divides each element of the given matrix by 2 in place, iterating column by column and row by row.
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0]) if n_rows > 0 else 0

    for j in range(n_cols):
        for i in range(n_rows):
            matrix[i][j] /= 2.0
    # 5000x5000 matrix: 6.255559730529785 seconds

def divide_by_two_numpy(matrix: np.ndarray):
    """
    Divides each element of the given matrix by 2 in place using numpy
    """
    matrix /= 2.0
    # 5000x5000 matrix: 0.016971540451049805 seconds

def compare_matrix_operations():
    size = 1000
    runs = 10
    print(f"Matrix operations with a {size}x{size} matrix over {runs} runs")
    report_performance(runs, divide_by_two_row_column, [[float(i) for i in range(1, size)] for _ in range(size)])
    report_performance(runs, divide_by_two_column_row, [[float(i) for i in range(1, size)] for _ in range(size)])
    report_performance(runs, divide_by_two_numpy, np.array([[float(i) for i in range(1, size)] for _ in range(size)]))

    print("\nComparing division by 2 and more complex math operations:")
    report_performance(runs, divide_by_two_row_column, [[float(i) for i in range(1, size)] for _ in range(size)])
    report_performance(runs, do_math_row_column, [[float(i) for i in range(1, size)] for _ in range(size)])

    print("\nComparing math operations with and without numpy:")
    report_performance(runs, do_math_row_column, [[float(i) for i in range(1, size)] for _ in range(size)])
    report_performance(runs, do_numpy_math_row_column, [[np.float64(i) for i in range(1, size)] for _ in range(size)])


if __name__ == "__main__":
    compare_matrix_operations()
