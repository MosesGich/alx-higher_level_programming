#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for f in sorted(list(a_dictionary)):
        print("{}: {}".format(f, a_dictionary[f]))
