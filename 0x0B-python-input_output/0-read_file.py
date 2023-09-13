#!/usr/bin/python3

"""
File handeling: open file

"""


def read_file(filename=""):
    """
    read the content within a file and print it to stdout

    Args:
        filename (str): the file to open and read from
    """

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
