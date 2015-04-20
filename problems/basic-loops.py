"""
Basic Problems involving For Loops
==================================

This file contains a set of functions which need to be completed so that they
perform the task outlined in the docstring.

Each docstring contains examples of what your code should do, which look like:

    >> some_function(some_value)
    some_output

These are used in the testing functions, don't change them!

To test all your code when you've finished - just call run_examples()
"""

# ======================= TESTING - IGNORE ===================================
import doctest
def run_examples():
    """This function just tests all the code - don't make any changes!"""
    print('Testing examples:')
    doctest.testmod()


# ========================== Start here ======================================


def seven_times(a, b):
    """
    PRINT the seven times table, for multiples between 7*a and 7*b.
    The times table should be printed in the same format as seen in the
    tutorial notes.
    >>> seven_times(3, 5)
    3 x 7 = 21
    4 x 7 = 28
    5 x 7 = 35
    >>> seven_times(99, 100)
    99 x 7 = 693
    100 x 7 = 700
    """

    return


def fizzbuzz_sum(n):
    """
    Find the sum of all the positive integers less than n that are either
    a multiple of 3 or 5 or both.
    >>> fizzbuzz_sum(20)
    78
    >>> fizzbuzz_sum(100)
    4635
    """

    return


def arithmetic_sum(a, d, n):
    """
    An arithmetic sequence starts with the number a, goes up each time by d,
    and has n terms, e.g. if a = 3, d = 2, n = 7 the sequence will be:
    3, 5, 7, 9, 11, 13, 15
    Find the sum of the sequence
    >>> arithmetic_sum(3, 5, 20)
    1010
    >>> arithmetic_sum(14, 23, 80)
    73800
    """

    return


def factorial(n):
    """
    The factorial of a number is calculated by multiplying all the
    positive integers smaller than that number together, e.g.
    5! (factorial) = 5 x 4 x 3 x 2 x 1.
    Return the factorial of n (assume n is a positive integer).
    >>> factorial(5)
    120
    >>> factorial(12)
    479001600
    """

    return
