#!/usr/bin/python3

'''
Print the alphabet in lowercase letters except "e" and "q"
'''

for i in range(97, 123):
    # Using ternary operator to test if the current character is not e or q
    # If true we print an empty string insted

    print("{}".format(chr(i) if chr(i) not in "qe" else ""), end="")
