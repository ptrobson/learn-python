---
layout: post
title: Formatting Strings
---

In the past, when we have wanted to produce strings that contain variables we
have usually cobbled them together using the '+' operator, and the 'str()'
function (for numerical variables), like so:

``` python
    num = 5
    animal = "squirrel"
    some_string = "There are " + str(num) + " " + animal + "s."
```

Obviously, this can get a little awkward when we want to create more complex
strings.  Thankfully, there is a better way.  Strings have a **format** method,
which will insert variables into the string at certain points indicated by
curly brackets like **{0}**.  For example:

``` python
    num = 5
    animal = "squirrel"
    some_string = "There are {0} {1}s.".format(num, animal)
```

We have passed the **format** method two variables, the first one will replace
any instances of **{0}**, while the second will replace any instance of
**{1}**.

Similarly, if we wanted to create a string that said something like "The cat
sat on the mat." we could do it by:

``` python
    subject = "cat"
    verb = "sat"
    object = "mat"
    some_rhyme = "The {0} {1} on the {2}".format(subject, verb, object)
```

If we would like to use named fields, instead of numbered ones (analogous to
using a dictionary instead of a list), we can do that instead:

``` python
    x_value = 10
    y_value = 4
    coordinates = "The ship is at ({x}, {y})".format(x=x_value, y=y_value)
```


