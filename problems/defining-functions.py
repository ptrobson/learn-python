
"""
Basic Problems involving Functions
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


def say_hello(name):
    """ PRINT the string 'Hello, John' where *John* is given by the
        argument name.
        >>> say_hello("Bob")
        Hello, Bob
        >>> say_hello("Harry Potter")
        Hello, Harry Potter
    """

    return


def add_two(num):
    """ Given a starting number, RETURN two more than that number.
        >>> add_two(5)
        7
        >>> add_two(1234)
        1236
    """

    return


def product(a, b):
    """ Given two numbers, a and b, RETURN their product.
        >>> product(3, 5)
        15
        >>> product(12, 9)
        108
    """

    return


def swap(a, b):
    """ Given two items, return each of them, but in the
        opposite order.
        >>> swap(2, 7)
        (7, 2)
        >>> swap("World", "Hello")
        ('Hello', 'World')
    """

    return
