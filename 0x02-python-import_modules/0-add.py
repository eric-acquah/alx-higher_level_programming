#!/usr/bin/python3
from add_0 import add

'''
Print the sum of adding to varaibles
'''

if __name__ == "__main__":
    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
