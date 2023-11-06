#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myl = [3, 5, 6, 7, 10]
    myl2 = []
    for i in myl:
        if i % 2 == 0:
            myl2.append(True)
        else:
            myl2.append(False)
    return myl2
