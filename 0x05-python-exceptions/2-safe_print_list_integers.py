#!/usr/bin/python3

# Print the first x elements in a list
# in integer format only
# Return: the number of elements printed


def safe_print_list_integers(my_list=[], x=0):

    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (TypeError, ValueError):
                continue
        print('')
        return count

    except IndexError:
        raise
