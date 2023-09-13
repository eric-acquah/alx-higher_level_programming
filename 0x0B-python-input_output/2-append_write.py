#!/usr/bin/python3

"""
File handeling: Append to a file

"""


def append_write(filename="", text=""):
    """
    Append content to a file

    Args:
        filename (str): name of file

    Return:
        number of bytes appended
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
