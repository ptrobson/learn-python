"""
Basic Problems involving Strings
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


def first_four(word):
    """
    Return a string comprising the first four characters of word.
    >>> first_four("This is some text")
    "This"
    >>> first_four("Hello world")
    "Hell"
    """

    return


def html_encode(text, tag):
    """
    In HTML, text is encoding by adding tags to the beginning and end of the
    text.  For instance, to put some text in bold, we tag it as so:
    <b>Some text</b>, using <*> and </*> at the start and end.
    Given a tag, and the text, return the coded version.
    >>> html_encode("Some bold text", "b")
    "<b>Some bold text</b>"
    >>> html_encode("Lorem Ipsum", "i")
    "<i>Lorum Ipsum</i>"
    """

    return


def sized_concatenate(word1, word2):
    """
    Given two words, concatenate them together in order of their length, with
    the longest word going first.
    >>> sized_concatenate("Hello", "Sunshine")
    "SunshineHello"
    >>> sized_concatenate("Tyrannosaurus", "Rex")
    "TyrannosaurusRex"
    """

    return


def remove_ends(word):
    """
    Return the word, minus its first and last letters.
    >>> remove_ends("jump")
    "um"
    >>> remove_ends("escaped")
    "scape"
    """

    return


def pig_latin(word):
    """
    Words are translated to pig latin by moving the first letter of the
    word to the end and then appending 'ay' to it.
    Translate 'word' into pig latin and return the translation.
    >>> pig_latin("hello")
    "ellohay"
    >>> pig_latin("banana")
    "ananabay"
    """

    return


def shouting(text, is_shouting):
    """
    In the wonderful world of the internet, text all in CAPS is often taken
    as being someone SHOUTING!!!  Given some text, and a boolean variable,
    'is_shouting', return the text:
        - in UPPERCASE, followed by "!!!" if is_shouting is True
        - in lowercase is is_shouting is False
    >>> shouting("Loud noises", True)
    "LOUD NOISES!!!"
    >>> shouting("A whisper...", False)
    "a whisper..."
    """

    return










