#!/usr/bin/python3

"""
Script to divide a given matrix by a given dividisor

"""


def matrix_divided(matrix, div):
    """
    Divide each row by the div

    Args:
        matrix (list): a list of lists of integer/float numbers
        div (int/float): number to divide the matrix

    Return:
        A new matrix with the multipled values
    """
    err_msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg2 = "Each row of the matrix must have the same size"
    err_msg3 = "div must be a number"

    if matrix:
        size = len(matrix[0])
    else:
        raise TypeError(f"{err_msg1}")
    new_matrix = []

    if div is None or (type(div) is not int and type(div) is not float):
        raise TypeError(f"{err_msg3}")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for col in matrix:

        if size != len(col):
            raise TypeError(f"{err_msg2}")

        sub_matrix = []
        for data in col:

            if data is None or (type(data) is not int and type(data)
                                is not float):
                raise TypeError(f"{err_msg1}")
            else:
                sub_matrix.append(round(data / div, 2))

        new_matrix.append(sub_matrix)

    return new_matrix
