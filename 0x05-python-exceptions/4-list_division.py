#!/usr/bin/python3

# Divide elements in list 1 by elem in list 2
# Store the result in third list. If division fails, store 0 in list
# Return: The newly created list


def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    prod = 0

    try:
        for i in range(list_length):
            try:
                prod = my_list_1[i] / my_list_2[i]
                new_list.append(prod)
            except (TypeError, ValueError):
                print("wrong type")
                new_list.append(0)
                continue
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
                continue

    except IndexError:
        print("out of range")
    finally:
        return new_list
