!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        Function that calculates fewest number of operations that are
        needed to give a result of exactly n characters in a file

        return:
               number of min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counteri
