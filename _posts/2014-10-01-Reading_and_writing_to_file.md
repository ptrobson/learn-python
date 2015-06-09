---
Layout: post
Title: Reading and writing to files
Tags: Files
---

Working with text files is very simple in python.  In this tutorial, I will
show you how to read and write files.

## Opening a file

To do anything with a file, we must first open it. The proper way to do this
in python is:

~~~ python

    with open("filename.txt") as my_file:

        # do some stuff with the file
~~~

There are other ways of opening files in python, but these all rely on you
ensuring the file gets closed properly at the end (and ensuring it gets closed
even in the event of errors etc.).

The 'with' statement ensures that the file gets closed properly whatever.
Anything that you want to do with the file must be inside an indented block
after the 'with'.  Once we have finished this block the file will close.


## Reading a file

If we want to read the contents of the file, there are several methods
depending on how much we want to read.  If we would like the whole contents
read in at once, we can:

~~~ python

    with open("filename.txt") as my_file:
        contents = my_file.readlines()
        print(contents)

~~~

This will produce a list containing all of the lines in the file.  Notice that
each line ends in a line-end character: "\n".

If we would like to just read a line at a time, we can do that by using
**readline** instead of **readlines**:

~~~ python

    with open("filename.txt") as my_file:
        first_line = my_file.readline()
        second_line = my_file.readline()

~~~


If we want to read in a very large file and just need to process a line at a
time, we can also iterate over the file like so:

~~~ python

    with open("filename.txt") as my_file:
        for line in my_file:
            print(line)

~~~

This last method is often the most useful.  Notice how when we print each line,
we get a blank line following it?  This is because our line still includes a
line-end character "\n".  We often won't want to include this in any
text-processing we do; so we can get rid of it using **strip**:

~~~ python

    with open("filename.txt") as my_file:
        for line in my_file:
            print(line.strip("\n"))

~~~



## Opening a file for writing

Writing to a file works very similarly to reading.  However, when we open the
file we need to tell it we want to open in **w**rite mode (we didn't need to
tell the computer what mode we were using earlier because it defaults to
**r**ead mode).  To do this we add the "w" argument to our open statement.

~~~ python

    with open("filename.txt", "w") as my_file:

        # write some stuff.

~~~

**Caution**: Be careful opening files in write mode - it will truncate
(**DELETE!**) the contents of the file and write over it.  If we want to open
the file to add extra text to it, we need to open it in **a**ppend mode.

~~~ python

    with open("filename.txt", "a") as my_file:

        # append some stuff to the end of the file

~~~


## Writing to a file

Writing to a file is very similar to reading one.  If I would like to add a
single line to my file, I 'write' to it:

~~~ python

    with open("filename.txt", "a") as my_file:

        my_file.write("Some text")
        my_file.write("And some more")

~~~

Notice that when we run this code, it does not add newline characters.  If we
want to start a new line in our code, we need to add those in ourselves:

~~~ python

    with open("filename.txt", "a") as my_file:

        my_file.write("A line\n")
        my_file.write("And another line\n")

~~~

If we would like to write more than one line at a time to the file, we can do
that with 'writelines':

~~~ python

    text = ["Line 1", "Line 2", "Line 3"]

    with open("filename.txt", "a") as my_file:

        my_file.writelines(text)

~~~

We may want to iterate through though, and add an end-line character to each
line before we write it:

~~~ python

    text = ["Line 1", "Line 2", "Line 3"]

    with open("filename.txt", "a") as my_file:

        for line in text:
            my_file.write(line + "\n")

~~~



