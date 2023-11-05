#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) < 2:
        print("")
        exit(0)
    for i in matrix:
        print("{:d} {:d} {:d}".format(i[0], i[1], i[2]))
