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
curly brackets like **{}**.  For example:

``` python
    num = 5
    animal = "squirrel"
    some_string = "There are {} {}s.".format(num, animal)
```

We have passed the **format** method two variables, the first one will replace
the first instance of **{}**, the second one will replace the second instance
of **{}** in the string.

We may not just want to insert items in that exact order though, or we may want
to use the variables multiple times. If that is the case, we can number the
points where we want to insert each item, and the corresponding argument will
be entered there.  For example:

``` python
    num = 1
    item = "Justin Bieber"
    some_string = "{0} {1} is {0} {1} too many!".format(num, item)
```

If we would like to use named fields, instead of numbered ones (just like when
we use a dictionary instead of a list), we can do replace the numbers with
names:

``` python
    latitude = 27.2
    longitude = -69.3
    coordinates = "The ship is at ({lat}, {long})".format(lat=latitude,
    long=longitude)
```

###
[Problems](https://raw.githubusercontent.com/andrewcharlton/learn-python/master/problems/string-formatting.py)

Click on the link above for problems that involve using these techniques.
