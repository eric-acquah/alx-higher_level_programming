#!/usr/bin/python3

# raise a type exception


def raise_exception():
    try:
        raise TypeError
    except TypeError:
        raise
