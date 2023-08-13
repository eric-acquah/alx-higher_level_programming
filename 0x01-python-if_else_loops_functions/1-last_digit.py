#!/usr/bin/python3
import random

'''
Print the last digit of the randomly generated number

If number is 0: print is zero
If number is > 5: print is greater than 5
If number is < 6 and not 0: print is less than or 6 and not zero
'''
number = random.randint(-10000, 10000)
last_msg = "Last digit of"
less_than_6 = "less than 6 and not 0"
last_digit = str(number)
last_digit = int(last_digit[-1])

# in case number is negative, convert last_digit to negative
if number < 0:
    last_digit = last_digit * -1

if last_digit == 0:
    print(f"{last_msg} {number:d} is {last_digit:d} and is 0")
elif last_digit < 6 and not 0:
    print(f"{last_msg} {number:d} is {last_digit:d} and is {less_than_6}")
elif last_digit > 5:
    print(f"{last_msg} {number:d} is {last_digit:d} and is greater than 5")
