#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# This program checks if the number is positive or negative

if number < 0:
    print(f"{number:d} is negative")
elif number > 0:
    print(f"{number:d} is positive")
else:
    print(f"{number:d} is zero")
