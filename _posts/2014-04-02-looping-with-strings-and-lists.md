---
layout: post
title: Looping with strings and lists
tags: Iteration Strings Lists
---

If we are working with lists, it is very common that we might want to do
something with each item in the list. Similarly, with strings, we might
want to look at each character in the string and do something with that.
We can use a for loop to do this very easily.  There are several methods of
achieving this, detailed below.


## Iterating using indexes.

The most obvious method of iterating through a list/string is to use their
indexes, and a range:

~~~ python

    some_list = [1, 2, 5, 8]
    size = len(some_list)
    for n in range(size):
        print(some_list[n])

~~~

This method is appropriate at times, if we're doing a sort for instance, but
is cumbersome a lot of the time.  Use this method only if you have to.  I'm
struggling to think of a good reason to ever use this with a string.


## Iterating through the items/characters

A much more concise way of doing this, if we just want to loop through each
item, and don't care where they are in the list/string, is to do the
following:

~~~ python

    some_list = [1, 2, 5, 8]
    for item in some_list:
        print(item)

    some_string = "ajhrk"
    for char in some_list:
        print(char)

~~~

This code will loop through each item in the list/string and just print them.
Obviously, we could do whatever we wanted with them.  Note: the variable names
**item** and **char** are entirely arbitrary, call them whatever you want
(within reason!).


## Iterating when you also need the position

If we also care about the position each item is in within the list/string,
we can use python's builtin **enumerate** function.  This returns both the
index and value of an item in a list/string.

~~~ python

    some_list = [1, 2, 5, 8]
    for index, item in enumerate(some_list):
        print("Item", index, "is", item)

    some_string = "ajhrk"
    for index, char in enumerate(some_string):
        print("Character", index, "is", char)

~~~

Again, the names **index**, **item** and **char** are entirely arbitrary.



###
[Problems](https://raw.githubusercontent.com/andrewcharlton/learn-python/master/problems/loops-with-strings-and-lists.py)
