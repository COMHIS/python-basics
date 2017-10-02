## Importing modules

In our Dostoyevsky -case previously, we had a line like this at the very top:

```python
from intros import read_txt_file_to_list
```

On that line we imported the command `read_txt_file_to_list` from another python -file, namely intros.py - note how the import command started with `from intros import ...`, pretty clear English, right? After importing, the function can now be used in our current script. That we did, on line 13 of [dostoyevsky1.py](../2_basic_concepts/dostoyevsky1.py).

Why is this importing useful then? Why didn't we just define the functions in [intros.py](../2_basic_concepts/intros.py) in the same script file as the rest of the code? There are a few good reasons to do this: First one is that very fast, one script file becomes rather big, and having all the code in one location can get messy fast. But the main reason is that we'll want to reuse many of the functions that we've written in multiple scripts. A general function for reading or writing text files, like the ones in intros.py, can be useful in a lot of different scripts. Therefore keeping them in a separate "module" of commands to be imported when needed can help us keep better organized, and save a lot of cutting and pasting. 

In addition to importing commands that we have created ourselves, like in the above case, we'll also be importing commands from modules written by others. There's a big collection of modules called [Python standard library](https://docs.python.org/3/library/index.html), that will carry us a long way. A few examples are: `csv` and `json` for parsing and writing structured data (think Excel) `datetime` for operating with dates, and `os` for operating with the computer filesystem (among other things). Commands from these modules are imported in a similar way:

```python 
# we're importing commands for dealing with timezones from datetime:
from datetime import timezone
```

We can also import whole modules if we want to use multiple commands contained in them, or we just don't care that we are bringing in some extra stuff that we won't be using:

```python 
# Let's load the csv-module to read some data from a table saved as .csv -file
import csv

# and we'll start using those commands here:
with open('some.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
...
```