#!/usr/bin/python3

'''
Print numbers from 00 to 89 without printing two
repeating numbers such as '10' and '01'
'''
for i in range(9):
    for j in range(i + 1, 10):
        if i == 8:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
