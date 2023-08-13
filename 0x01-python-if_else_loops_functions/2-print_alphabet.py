#!/usr/bin/python3

'''
Function to print the ascii alphabet characters in lowercase
'''
for i in range(ord('a'), (ord('z') + 1)):
    print("{:c}".format(i), end="")
