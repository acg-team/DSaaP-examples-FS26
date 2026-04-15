#!/usr/bin/env python

import math as m
from time import sleep

def do_silly_stuff(value: float) -> float:
    """
    Simulates a time-consuming operation by performing some math.
    """
    return value * value + m.sin(value) + m.cos(value)


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
        matrix[i][0] = do_silly_stuff(matrix[i][0])
        for j in range(n_cols):
            matrix[i][j] = \
                do_math(matrix[i][j])


if __name__ == "__main__":
    size = 10000
    do_math_row_column([[float(i) for i in range(1, size)] for _ in range(size)])
