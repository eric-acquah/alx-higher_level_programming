#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if not len(matrix) == 1:
        for ex_arr in matrix:
            for in_arr in ex_arr:
                print("{:d}".format(in_arr), end="\n" if in_arr == ex_arr[-1]
                      else " ")
