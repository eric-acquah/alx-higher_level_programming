#!/usr/bin/python3
import hidden_4

'''
Print names within the imported moudle
*Print all names except names that start with "__"
*Print in alphabetically sorted order
'''


def print_hidden():

    # Print all names within hidden_4
    for name in dir(hidden_4):
        # if the first two characters are "__" skip
        if name[:2] == "__":
            continue
        print(name)


if __name__ == "__main__":
    print_hidden()
