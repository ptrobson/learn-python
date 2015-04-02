"""
String Formatting Problems
==========================

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

def egg_basket(item, container):
    """
    PRINT the string "Don't put all your eggs in one basket", where the words
    'egg' and 'basket' are given by item and container respectively.
    >>> egg_basket('eggs', 'basket')
    Don't put all your eggs in one basket
    >>> egg_basket('money', 'bank')
    Don't put all your money in one bank
    """

    return


def bottles_of_beer(n):
    """
    PRINT the string "n bottles of beer on the wall, n bottles of beer!"
    >>> bottles_of_beer(10)
    10 bottles of beer on the wall, 10 bottles of beer!
    >>> bottles_of_beer(5)
    5 bottles of beer on the wall, 5 bottles of beer!
    """

    return


def introductions(name1, name2):
    """
    PRINT the string "John meet Andy, Andy meet John." where the names John
    and Andy are given by name1 and name2 respectively.
    >>> introductions("Bob", "Amelia")
    Bob meet Amelia, Amelia meet Bob.
    >>> introductions("Helen", "Nick")
    Helen meet Nick, Nick meet Helen.
    """

    return


def sum_and_product(a, b):
    """
    PRINT the string "5 + 3 = 8, 5 x 3 = 15", where the numbers 5 and 3 are
    given by a and b respectively.
    >>> sum_and_product(12, 8)
    12 + 8 = 20, 12 x 8 = 96
    >>> sum_and_product(53, 97)
    53 + 97 = 150, 53 x 97 = 5141
    """


    return
