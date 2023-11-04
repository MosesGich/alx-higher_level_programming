#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    mylist2 = []
    mylist2 = my_list.copy()
    mylist2[idx] = element
    return mylist2
