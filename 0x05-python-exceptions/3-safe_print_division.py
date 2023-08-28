#!/usr/bin/python3

# Print the result of division
# Return: result of division


def safe_print_division(a, b):

    result = None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
