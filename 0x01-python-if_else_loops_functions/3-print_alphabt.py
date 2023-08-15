#!/usr/bin/python3

'''
Print the alphabet in lowercase letters except for "e" and "q"
'''

for i in range(ord('a'), (ord('z') + 1)):
    # Using ternary operator to test if the current character is not e or q
    # If true we print an empty string insted

    print("{}".format(chr(i) if chr(i) not in "qe" else ""), end="")
