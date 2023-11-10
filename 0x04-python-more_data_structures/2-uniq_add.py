#!/usr/bin/python3
def uniq_add(my_list=[]):
    newl = []
    mysum = 0
    for n in my_list:
        if n in newl:
            continue
        else:
            newl.append(n)
            mysum += n
    return mysum
