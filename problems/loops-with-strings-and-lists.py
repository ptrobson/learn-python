"""
Looping with Strings and Lists
==============================

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


def e_words(words):
    """
    Given a list of words, count the number that contain an 'e' or 'E'.
    >>> e_words(['mary', 'had', 'a', 'little', 'lamb'])
    1
    >>> e_words(['Peter', 'Piper', 'picked', 'a', 'peck', 'of', 'pepper'])
    5
    """

    return


def short_and_sweet(words, length):
    """
    Given a list of words, create a string (seperated by spaces) of all the
    words with a size less than length.
    >>> short_and_sweet(['A', 'hugely', 'big', 'orange', 'elephant', 'pet'], 4)
    'A big pet'
    >>> short_and_sweet(['Go', 'down', 'to', 'this', 'dark', 'sea'], 4)
    'Go to sea'
    """

    return


def list_average(numbers):
    """
    Given a list of numbers, return their average (mean), rounded down to the
    nearest integer.
    >>> list_average([4, 7, 9])
    6
    >>> list_average([3, 3, 5, 10])
    5
    """

    return


def letter_location(string, letter):
    """
    Given a string, find all the occurences of 'letter' and add up the
    index values of the places where they occur.  Return this sum.
    >>> letter_location('hello billy', 'l')
    22
    >>> letter_location('why oh why', 'y')
    11
    """

    return


def weighted_sum(numbers):
    """
    A list is used to keep track of scores students achieve in tests and
    homeworks.  The scores alternate between homework and assessment results,
    with the first score being a homework.
    Assessment scores are worth double homework scores.
    Every 3rd assessment is a mock exam, worth triple points.
    Find the weighted sum of the scores, ie. Homeworks + 2 x Tests + 3 x Mocks
    >>> weighted_sum([5, 8, 7])
    28
    >>> weighted_sum([3, 4, 2, 5, 8, 6, 9])
    58
    """

    return


def html_parse(string):
    """
    HTML uses tags such as <b> to apply formatting, hyperlinks etc. to content
    on websites.  Given a string of HTML, return an output string stripped of
    all the tags.  Anything enclosed between '<' and '>' should be discarded.
    >>> html_parse("This is some <b>bold text</b>, and <i>italics!</i>")
    'This is some bold text, and italics!'
    >>> html_parse("<a href=www.google.com>Link to <b>GOOGLE</b></a>")
    'Link to GOOGLE'
    """

    return


def odd_letters(words):
    """
    An *odd letter* in a word is defined as one where the index of that letter
    is odd, e.g. in 'abcde', 'b' and 'd' are the odd letters.
    Similarly, an *odd word* in a list is one where the index of that word
    is odd.
    Create a string composed of all the odd letters in the odd words.
    >>> odd_letters(['This', 'is', 'quite', 'hard'])
    'sad'
    >>> odd_letters(['Do', 'we', 'need', 'some', 'nesting?'])
    'eoe'
    """

    return
