#!/usr/bin/python3

"""
File handeling - write to a file

"""


def write_file(filename="", text=""):
    """
    write text to a file

    Args:
        filename (str): file to write to
        text (tet): text to write into

    Return:
        The number of bytes read
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
