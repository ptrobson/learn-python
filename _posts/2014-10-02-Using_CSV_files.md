---
Layout: post
Title: Using CSV files
Tags: Files
---

If you are working with basic textual/numerical data, CSV files are a simple
solution to storing that data.  In this tutorial, we will look at reading and
writing data to a csv file.

## What is a CSV file?

CSV stands for Comma-Separated Values.  In a CSV file, data is stored with each
field being separated by commas (usually, although other delimiters can be
used).  In plain-text, a csv file might look like:

~~~

Name, Age, Score
John, 12, 53
Adam, 13, 47
Charlotte, 15, 65

~~~

## The csv module

Python has a handy module, csv, which helps us read an write to csv files.
To use this module, simply add the following line to the top of your script:

~~~ python

    import csv

~~~

Be careful that you don't name any of your files 'csv.py' when playing with
this, because that will conflict with the proper module and stop it importing.


## Reading CSV files

To read a csv file in, with each field separated, we can use the 'csv.reader'
function.  This allows us to loop through each field in our file, and do
something with the data.

~~~ python

    with open("filename.csv") as my_file:

        reader = csv.reader(my_file)
        for line in reader:
            print(line)

~~~

If our csv file has a header line that we want to ignore, we can always read
one (or more) lines of our file, before creating the reader:

~~~ python

    with open("filename.csv") as my_file:

        my_file.readline()

        reader = csv.reader(my_file)
        for line in reader:
            print(line)

~~~

Notice that each line is a list of data, with each field one item in the list.
Be aware that all of the data is read in as strings - if the data is numerical,
you will need to convert it to either an integer or a float before you use it.


## Writing CSV files

Similarly, to write a csv file, we can use the 'csv.writer' function.

When opening a csv file for writing on Windows, it will put an extra line in
between lines.  We can get around this by specifying an extra 'newline'
parameter when we open the file:

~~~ python

    with open("filename.csv", "a", newline="\n") as my_file:

        writer = csv.writer(my_file)
        writer.writerow([1, 2, 3])

~~~

The csv.writer will be expecting a list to write to the file.  If you supply it
with a string, it will split it into characters.  If you supply it with
something like a number you will get an error.


To write multiple more than one record to the file at a time, we can use the
'writerows' function:

~~~ python

    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    with open("filename.csv", "a", newline="\n") as my_file:

        writer = csv.writer(my_file)
        writer.writerows(data)

~~~


