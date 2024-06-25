#!/usr/bin/python3
"""Rotate 2D Matrixs"""


def rotate_2d_matrix(matrix):
    """rotate a 2d matrix

    Args:
        matrix (List[]): nxn matrixs
    returns:
        matrix(List[]): 90degree rotated matrixs
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reversing each row in-place
    for row in matrix:
        row.reverse()

    return matrix
