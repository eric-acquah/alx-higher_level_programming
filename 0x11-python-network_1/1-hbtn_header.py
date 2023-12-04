#!/usr/bin/python3

"""
Fetch for data from the response header

"""


import urllib.request
import sys


if __name__ == '__main__':
    link = sys.argv[1]

    with urllib.request.urlopen(link) as resource:
        target_head = resource.info()

        print(target_head['X-Request-Id'])
