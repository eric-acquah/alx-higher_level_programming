#!/usr/bin/python3

"""
Execute select query on a given database

"""

import MySQLdb
import sys


if __name__ == '__main__':
    user_name = sys.argv[1]
    key = sys.argv[2]
    user_db = sys.argv[3]

    connection = MySQLdb.connect(
        host='localhost',
        user=user_name,
        port=3306,
        passwd=key,
        db=user_db
    )

    cursor = connection.cursor()

    query = 'SELECT * FROM states WHERE name COLLATE utf8mb4_bin \
LIKE "N%" ORDER BY states.id'

    cursor.execute(query)  # query the database
    output = cursor.fetchall()

    # Print output
    for row in output:
        print(row)

    # cleanup action
    cursor.close()
    connection.close()
