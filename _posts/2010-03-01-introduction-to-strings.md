---
layout: post
title: Introduction to Strings
tags: Strings
---

A string is the computing name for a piece of text.  In this lesson we will
look at how we can manipulate strings in various ways: concatenation, splicing,
changing case etc.

## Creating and Adding Strings

Creating a string is very simple:

~~~ python

    some_string = "A bunch of text"
    another_string = 'Some more text'

~~~

The use of double ("") or single ('') quotes is almost entirely a style choice,
feel free to use whichever you would like.

Adding two strings together works in exactly the way you would imagine as well:

~~~ python

    string_1 = "Hello"
    string_2 = " World"
    output = string_1 + string_2
    print(output)

~~~

If we want to append something to the end of a string, we can also use the
**+=** operator.

~~~ python

    string_count = "One"
    string_count += " Two"
    string_count += " Three"
    print(string_count)

~~~

We can even multiply strings:

~~~ python

    a_string = "Hi ho "
    output = a_string * 2
    print(output)

~~~

## Finding the length of a string

If we need to find the length of a particular string, we can use the **len**
function:

~~~ python

    a_long_string = "How long is a piece of string?"
    print(len(a_long_string))

~~~


## Picking out individual characters in a string

A string can be considered as an ordered set of characters.  If we want to use
a character in a particular place in a string, we can get to it like so:

~~~ python

    the_alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(the_alphabet[2])

~~~

The square brackets tell us to pick a particular part of the string out, the
number tells us which character.  The first character in any string is
character 0, so character 2 will actually be the **third** one.

We can also count backwards from the end of the string using a negative index:

~~~ python

    the_alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(the_alphabet[-1])
    print(the_alphabet[-3])

~~~

## Splicing Strings

If we want a section of a string, rather than just a single character, we can
create a **splice**.  To do this, we use the square brackets but this time we
provide a range:

~~~ python

    the_alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(the_alphabet[2:5])

~~~

Notice that the splice does not include the character at position 5.  It starts
at character 2 and gives all the characters up to, but not including, the end
of the range.

If we want all of the characters from either the beginning or end of the
string, we can leave one of the parameters blank:

~~~ python

    the_alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(the_alphabet[20:])
    print(the_alphabet[:6])

~~~

We can also use negative numbers in the range given for a splice.


## Playing with case

If we want to change the case of our string, python has several built in
functions to do so:

~~~ python

    a_mixed_string = "A string with RANDOM Capital Letters"

    lowercase_string = a_mixed_string.lower()
    print(lowercase_string)

    uppercase_string = a_mixed_string.upper()
    print(uppercase_string)

    capitalised_string = a_mixed_string.capitalize()
    print(capitalised_string)

    titlecase_string = a_mixed_string.title()
    print(titlecase_string)

~~~

