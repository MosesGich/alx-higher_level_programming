#!/usr/bin/python3
def no_c(my_string):
    mylist = [x for x in my_string if x != 'c' and x != 'C']
    newstring = ''.join(mylist)
    return newstring
