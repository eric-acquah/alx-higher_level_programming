#!/usr/bin/python3
import sys

# Print the given value in integer format
# Return: true if successful else false


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
