#!/usr/bin/python3
'''Add integers module'''


def add_integer(a, b=98):
    '''Add two numbers.
    Args:
        a: first integer number
        b: second integer number
    Raises:
        TypeError: If a or b is not an integer value
    Returns:
        The addition of supplied arguments
    '''
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    return int(a + b)
