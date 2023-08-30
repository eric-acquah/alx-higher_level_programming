#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if len(matrix[0]) == 0:
        print('')
        return
    for ex_arr in matrix:
        for in_arr in ex_arr:
            print("{:d}".format(in_arr), end="\n" if in_arr == ex_arr[-1]
                  else " ")
