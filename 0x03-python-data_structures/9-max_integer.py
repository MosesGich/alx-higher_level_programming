#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    f = my_list[0]
    for x in my_list:
        if x > f:
            f = x
    return f
