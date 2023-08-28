#!/usr/bin/python3

# Print out a given value in integer format only
# Return: True if succesful else False


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True


    except Exception:
        return False
