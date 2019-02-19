"""
Functions that return fibonacci & lucas numbers
"""


def fibonacci(n):
    """ accepts integer n, returns nth fibonacci number """
    first, second = 0, 1
    for i in range(n - 1):
        first, second = second, first + second
    return first
