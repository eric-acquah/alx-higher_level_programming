#!/usr/bin/python3

'''
Print the alphabet in lowercase letters except for "e" and "q"
'''

for i in range(ord('a'), (ord('z') + 1)):
    if chr(i) not in "qe":
        print("{:c}".format(i), end="")
