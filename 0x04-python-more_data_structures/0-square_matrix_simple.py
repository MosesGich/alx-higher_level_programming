#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = [[x*x for x in row] for row in matrix]
    return m
