#!/usr/bin/python3

# raise a name exception with message


def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError:
        raise
