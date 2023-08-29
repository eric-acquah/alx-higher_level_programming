#!/usr/bin/python3
import sys

# excute functions safely
# Return: result of the function if succesful else None


def safe_function(fct, *args):

    result = ""
    try:
        result = fct(*args)
        return result
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
