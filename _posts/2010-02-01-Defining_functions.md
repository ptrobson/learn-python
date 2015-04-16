---
layout: post
title: Defining Functions
tags: Functions
---

There is a tendency for people, when they first learn to program, to write a
single long script to accomplish what they want to do. This is almost never
the best way to go about solving a problem, and will often make the code
overly complicated to understand.  Before you sit down and start coding,
STOP!  Think about what you want your code to do overall, and the different
tasks necessary to accomplish that task.

## Creating and Calling Functions

In python, we use **Functions** to break up our code into different parts. A
function is created like so:

~~~ python

    def function_name():

        do some stuff

~~~

The **def** keyword shows that we want to create a new function. We then
give the function a name, and follow this with **():** (more on this later).
Anything that we want the function to do, we **indent** (this means add some
extra spaces, usually 4, at the start of each line).  The function will
be assumed to be finished when our indentation moves back to the same
level as the **def** keyword was.

For instance, we could create a function to say hello to someone:

~~~ python

    def say_hello():

        name = input("What is your name: ")
        print("Hello", name)

~~~

Now, this will just define the function.  If we actually want to run it,
we need to **call** it, like so:

~~~ python
    
    say_hello()

~~~

## Using arguments

In the previous example, our function asked the user for their name.
In most real-life programs though, information like that would probably
be already available, stored in a customer database for example. We would
like to be able to use that information in our function. To do that, we can
give our function **arguments**.  These are variables that are passed to the
function, and we define them inside the brackets that we saw earlier.

If we wanted to rewrite our earlier function using an argument, it would
look like this:

~~~ python

    def say_hello(name):

        print("Hello", name)

~~~

To call our function now, we must supply it with an argument like so:

~~~ python

    say_hello("John")

~~~


## Returning Values

If our function does something like performing a calculation which produces
a result, we would probably like to do something with that result.  In
cases like these, we can **return** the result from our function.

~~~ python

    def add(a, b):

        return a + b

~~~

Note that when we **return** from a function, it is assumed that the function
has finished.  Any code after that will not run.  This can be very useful
if you're writing a function that continues until certain conditions are met.
In cases like these, we would return when the conditions are met so that
the functions terminates.

To use the result from a function, we need to assign it to a variable like so:

~~~ python

    result = add(5, 7)

~~~

We can now use this variable in any further calculations.


## Multiple return values

If our calculations provide more than one useful result, we can return them
all. To do this, simply return all the variables seperated by commas:

~~~ python

    def divide(a, b):

        quotient = a // b        # // Finds the whole number part of a division
        remainder = a % b        # % Finds the remainder of a division
        
        return quotient, remainder

~~~


To use those values, we can assign them to multiple variables when we call
the function:

~~~ python

    quot, rem = divide(10, 3)
    print("10 divided by 3 is", quot, "remainder", rem)

~~~

Note, the variable names don't have to be the same when we return from the
function and call it.  The order must be the same though!


## Using functions

When writing a program, try to seperate out each piece of logic and put it
in its own little function. This will make your code much easier to understand,
test and debug.  Once you've defined functions, you can use them inside other
functions; they can even be used inside themselves (this is called *recursion*,
and is a bit more advanced!). If you find yourself repeating code, particularly
if you're just copy-pasting from one place to another - put that code inside a
function and call it.  It will be much easier in the long run, promise!


###
[Problems](https://raw.githubusercontent.com/andrewcharlton/learn-python/master/problems/defining-functions.py)
