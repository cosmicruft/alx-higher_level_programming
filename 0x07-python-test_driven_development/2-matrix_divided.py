#!/usr/bin/python3
'''
     division of all elements of a matrix.
'''


def matrix_divided(matrix, div):
    '''
        A function that divides all elements of a matrix.
        Args:
            matrix: a 2 by 2 array or list of elements
            div: the divisor
        Raises:
            TypeError: if matrix is not a list of lists
            TypeError: elements are neither int or float
            TYpeError: lists are not of equal size
            TypeError: if div is not number
            ZeroDivisionError: if div is zero
        Returns: A new matrix
    '''
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not matrix or type(matrix) != list):
        raise TypeError(msg)
    if type(div) not in (float, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for array in matrix:
        if type(array) != list or len(array) == 0:
            raise TypeError(msg)
        if len(array) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
            for element in array:
                if not isinstance(element, (float, int)):
                    raise TypeError(msg)
    c = list(map(lambda a: list(map(lambda b: round(b / div, 2), a)), matrix))
    return c
