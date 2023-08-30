#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    clist = my_list[::-1]
    for i in clist:
        print("{:d}".format(i))
