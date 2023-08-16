#!/usr/bin/python3
import sys

'''
Print the number and values of commandline arguments

*Print number of argument(s) (or argument if argv < 2)
*Print "position of element: value of element" on a newline
'''


def print_cmdline_args():

    arg_len = (len(sys.argv) - 1)

    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        # print '1 argument: and 1: argument value'
        print("{0} argument:\n{0}: {1}".format(arg_len, sys.argv[1]))
    else:
        print("{} arguments:".format(arg_len))

        for i in range(1, (arg_len + 1)):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    print_cmdline_args()
