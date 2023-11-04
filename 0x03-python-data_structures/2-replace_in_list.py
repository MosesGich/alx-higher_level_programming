#!/usr/bin/python3
def replace_in_list(mylist, idx, element):
    if idx < 0 or idx > len(mylist) - 1:
        return mylist
    mylist[idx] = element
    return mylist
