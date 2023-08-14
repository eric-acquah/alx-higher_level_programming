#!/usr/bin/python3

'''
Print the alphabet in lowercase letters except for "e" and "q"
'''

for i in range(97, 123):
    if chr(i) not in "qe":
        print("{:c}".format(i), end="")
