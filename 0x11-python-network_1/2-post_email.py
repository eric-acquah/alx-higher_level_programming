#!/usr/bin/python3

"""
Pass data to server via http request

"""

import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    user_email = sys.argv[2]

    email_content = {'email': user_email}
    parsed_data = urllib.parse.urlencode(email_content)
    encoded_data = parsed_data.encode('utf-8')

    request = urllib.request.Request(url, encoded_data)

    with urllib.request.urlopen(request) as response:
        target_value = response.read()

        print(target_value)
