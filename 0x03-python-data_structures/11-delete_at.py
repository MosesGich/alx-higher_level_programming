#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list) - 1:
        return my_list
    i = 0
    for j in my_list:
        if idx == i:
            my_list.remove(j)
        i += 1
    return my_list
