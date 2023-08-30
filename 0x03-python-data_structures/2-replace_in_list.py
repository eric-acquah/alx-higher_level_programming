#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if not idx < 0 or len(my_list) >= idx:
        my_list[idx] = element
    return my_list
