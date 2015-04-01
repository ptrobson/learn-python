---
layout: post
title: Basic For Loops
draft: True
---

### Basics

One of the main advantages of using a computer to do anything, is that they
can repeat tasks again and again quickly and accurately.

If we know how many times we want to repeat something, we can use a **for**
loop. The basic syntax looks something like this:

``` python
    for n in range(5):
        print("Hello world")
```

This will print "Hello world" 5 times. 

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
in a for loop instead.
