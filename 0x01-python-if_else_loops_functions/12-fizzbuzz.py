#!/usr/bin/python3

'''
fizzbuzz - print from 1 to 100
For the multiples of 3 print "Fizz"
For the multiples of 5 print "Buzz"
For the multiple of both print "FizzBuzz"
'''


def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
    print('')
