#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    mys = set_1.difference(set_2)
    mys.update(set_2.difference(set_1))
    return mys
