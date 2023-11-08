#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx = my_list.index(search)
    myl = my_list.copy()
    myl[idx] = replace
    return myl
