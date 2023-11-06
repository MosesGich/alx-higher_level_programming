#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myl2 = []
    for i in my_list:
        if i % 2 == 0:
            myl2.append(True)
        else:
            myl2.append(False)
    return myl2
