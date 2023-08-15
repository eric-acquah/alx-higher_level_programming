#!/usr/bin/python3

'''
print_last_digit - print and return the last digit of a number
@number: number whose last digit is to be printed
'''


def print_last_digit(number):
    if number < 0:
        number *= -1
    last_digit = number % 10
    print("{:d}".format(last_digit), end="")

    return last_digit
