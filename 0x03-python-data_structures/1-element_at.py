#!/usr/bin/python3
def element_at(mylist, idx):
    if idx < 0 or idx > len(mylist) - 1:
        return None
    return mylist[idx]
