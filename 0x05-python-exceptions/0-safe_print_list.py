#!/usr/bin/python3

# Print x elements within a list a given list
# Return: the actual elements printed


def safe_print_list(my_list=[], x=0):

    count = 0
    try:
        for elem in range(x):
            print("{}".format(my_list[elem]), end="")
            count += 1
        print('')
        return count

    except Exception:
        print('')
        return count
