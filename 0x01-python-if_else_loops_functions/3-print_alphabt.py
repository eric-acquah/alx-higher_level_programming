#!/usr/bin/python3

'''
Print the alphabet in lowercase letters except for "e" and "q"
'''

for i in range(ord('a'), (ord('z') + 1)):
    if i != ord('e') or i != ord('q'):
        print("{:c}".format(i), end="")
