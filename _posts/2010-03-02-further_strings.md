---
layout: post
title: Useful string conditionals
tags: Strings
---

This tutorial brings together a few useful techniques for using strings in
conditionals.  These functions are very helpful when performing validation
checks on string input data.


## Checking for a substring

If we have a string, and would like to know whether a particular character (or
combination of characters), is somewhere within that string, we can use the
**in** keyword:

~~~ python

    a_string = "Hi ho, hi ho, it's off to work we go!"
    if "off" in a_string:
        print("Found off")

    if "hello" in a_string:
        print("Found hello")
~~~

If we would like to check whether a particular substring appears at the start
or end of a string, we can use the **startswith** and **endswith** functions.

~~~ python

    another_string = "this string both starts and ends with this"

    if another_string.startswith("this"):
        print("Starts with this")

    if another_string.endswith("this"):
        print("Ends with this")

~~~

## Checking for a particular type of string

If we would like to check whether a string is of a particular type, e.g. all
aphabetical, python has some built-in checking functions that we can use:

~~~ python

    some_string = "A random string"

    if some_string.isalpha():
        print("A string with just alphabetical characters")

    if some_string.isnumeric():
        print("A string with just numerical digits")

    if some_string.isalnum():
        print("A string with alphabetical and/or numerical characters")

~~~

## Checking for a particular case

If we would like to check whether a string is in a particular case, e.g. all
UPPERCASE, there are built-in functions for this too.  Note, these functions
only check the alphabetical characters - if a string also contains numerical
digits or punctuation, these will be ignored in the check.

~~~ python

    some_string = "Another random string"

    if some_string.isupper():
        print("An UPPERCASE string")

    if some_string.islower():
        print("A lowercase string")

    if some_string.istitle():
        print("A string in Titlecase")

~~~


