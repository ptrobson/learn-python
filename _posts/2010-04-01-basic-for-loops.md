---
layout: post
title: Basic For Loops
tags: Iteration
---

One of the main advantages of using a computer to do anything, is that they
can repeat tasks again and again, quickly and accurately.

## Using a 'for' loop

If we know how many times we want to repeat something, we can use a **for**
loop. The basic syntax looks something like this:

``` python
    for n in range(5):
        print("Hello world")
```

This will print "Hello world" 5 times. The indentation is important!  Just like
when we defined a function, the level of indentation shows which bit we want
to repeat and when to finish looping.  Anything that is indented will be
repeated, until we get to a statement that has the same level of indentation
as the **for** keyword.

We can see what's happening in a little more detail if we try:

```python
    for n in range(5):
        print(n)
```

range(5) generates 5 values, starting at 0 and finishing at 4. The loop
creates a variable, n, sets it equal to each of the values generated in turn
and runs the code with that variable.


### Printing the 7 times table

If we wanted to print the 7 times table, we could write some code that looked
like:

``` python
    print("1 x 7 = 7")
    print("2 x 7 = 14")
    print("3 x 7 = 21")
    ...
```

This code is obviously repeating itself considerably, and is ideal for putting
in a for loop instead. When trying to replace code like this, try and identify
what is changing on each loop - in this case, its the first and last numbers.
We could replace it with something like:

~~~ python

    for n in range(11):
        print(n, "x 7 =", n*7)

~~~

## More advanced ranges

Whilst the for loop we just used to print the times table was a significant
improvement on writing out each line individually, it did have one issue
with it - it prints out '0 x 7 = 0'.  *range(11)* starts at 0, and gives
all the numbers up to, but not including, 11. There will often be times
when we want to start at a different number, or even go up in steps of
more than 1.  Thankfully, this can be easily achieved by using additional
arguments on our range.

Using two arguments in our range function allows us to specify a **start** and
**end** point:

~~~ python
    for n in range(1, 11):
        print(n)

~~~

Using three arguments also allows us to change the **step** size:

~~~ python
    for n in range(1, 11, 2):
        print(n)

~~~

These numbers can also be negative (but must be integers).

~~~ python
    for n in range(10, 0, -1):
        print(n)

~~~

The general syntax for range then is one of:

~~~ python
    range(end)
    range(start, end)
    range(start, end, step)

~~~

If these arguments are not included, they default to 0 and 1 for the start and
step respectively.


## Counting and summing things in a loop

Let's say I want to add up all the numbers from 0 to 20.  To do this, I need
some variable to keep track of the running total, and then loop through each
number and add it on to the total.  I can do this like so:

~~~ python
    total = 0
    for n in range(21):
        total += n

    print(total)

~~~

Notice that I created, and initialised, my variable outside of the loop
initially. If we try to do it inside the loop, we will reset our variable
every time our loop makes a pass.  Remember, the **+=** operator increments
our variable by that amount.


###
[Problems](https://raw.githubusercontent.com/andrewcharlton/learn-python/master/problems/basic-loops.py)
