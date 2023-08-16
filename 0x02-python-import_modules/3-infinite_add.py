#!/usr/bin/python3
import sys

'''
Print the sum of all commandline integer arguments
'''


def print_all():
    # sum all arguments of agrv execpt for argv[0]

    arg_len = len(sys.argv)
    total = 0

    for i in range(1, arg_len):
        total += int(sys.argv[i])
    print("{:d}".format(total))


if __name__ == "__main__":
    print_all()
