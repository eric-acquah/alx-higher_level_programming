#!/usr/bin/python3

'''
Print numbers from 00 to 99 with "," and " " as delimeter
'''

f1 = 0
f2 = 0
delim = ", "

print("{}{}{}".format(f1,f2,delim), end="")

for i in range(99):

    if i == 98:
        delim = "\n"
    if f2 > 8:
        f1 += 1
        f2 = 0
    else:
        f2 += 1
    print("{0:d}{1:d}{2:s}".format(f1, f2, delim), end="")
