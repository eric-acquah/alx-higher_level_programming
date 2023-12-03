#!/usr/bin/python3

"""
Fetch the status of a web resource using urllib

"""

import urllib.request


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        status = response.read()
        decode = status.decode("utf-8")

    print("Body response:")
    print(f"    - type: {type(status)}")
    print(f"    - content: {status}")
    print(f"    - utf8 content: {decode}")
