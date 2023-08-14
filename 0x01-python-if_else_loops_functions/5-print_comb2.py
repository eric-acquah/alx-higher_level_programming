#!/usr/bin/python3

'''
Print numbers from 00 to 99 with "," and " " as delimeter
'''

f1 = 0
f2 = 0
delim = ", "

for i in range(99):

    if i == 98:
        delim = "\n"
    if f2 > 8:
        f1 += 1
    print("{:d}".format(f1), end="")
    if f2 > 8:
        f2 = 0
    else:
        f2 += 1
    print("{:d}{}".format(f2, delim), end="")
