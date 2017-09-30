# Part 3 - Basic concepts in programming II

This part will familiarize you with the second group of basic concepts. After understanding these, you are in theory ready to go. There is still a lot of ground to cover beyond these concepts, but for an aspiring digital humanist, you are basically ready to go.

---

## Concepts to be covered

blahblah. 

### Lists and dictionaries

The reason why programming is such a useful thing to learn, is that you are very soon able to automatise repetitive tasks. The amount of time you spend writing the code does not depend on the size of your dataset, and for most simpler tasks the computer can run through thousands of rows of data in seconds.

In order to get acquainted with handling datasets and their manipulation, we first take a look at the most common data structures implemented in Python to hold more variables than just one. They are called _lists_, _dictionaries_ and _tuples_.

Basically their idea is the same: you can refer to whole bunch of variables with just one name! Their differences comes from how you operate them and access the variables put into them.

**List**

List is simply just a batch, row, line, set or _list_ of things. Items in a list have order, and can be accessed by index based on that order, but that's about it.

A list in Python code is usually defined by encasing items in the list with square brackets and using comma as a separator.
Example here
```python
my_list = [1, 5, 8, 22, 4, 11]
```
would produce a list containing integers 1,5,8,22,4 and 11 in this order. Many useful functions return lists as their outcome, so for example very nifty _split_ function splits strings into lists. This way we can operate for example sentences as a list of words:

```python
sentence = "Introduction to Digital Humanities is teh best course I have ever been to."
sentence_as_list = sentence.split(" ")
print(sentence_as_list)
["Introduction", "to", "Digital", "Humanities", "is", "teh", "best", "course", "I", "have", "ever", "been", "to."]
```
To access any element of the list, you refer to it by its location in the list, called index. Like in many programming spheres, in Python the first index is always 0, the second 1 and so on. Element accessing is done by adding square brackets after the lists name, and inside the brackets go the index:

```python
first_word = sentence_as_list[0]
```
In addition to accessing a single element of a list, it is also possible to get a number of different subsets or slices of a list:

```python
print(sentence_as_list[0:3])
["Introduction", "to", "Digital"]
print(sentence_as_list[-1])
["to."]
print(sentence_as_list[10:])
["ever", "been", "to."]
```
In many programming languages, one list like object can hold only one (or predefined catalogue) type of variables. In Python this is not restricted and a list can hold any number of different kinds of things:

```python
miscellania = ["pears", 4, "not there yet", True, True, 0.1234984573]
```
Lists can hold even other lists!
```python
list_of_lists = [[0,2,3],[1,5,12], ["n/a", 22, 0]]
```
A common problem for any Excel-humanist is that the original data might contain in one column two variables. Imagine that you are researching book history and on one column of your otherwise flawless Excel-sheet you have the publication place written in the form of "City, Country". Like "Antwerpen, Netherlands", "Berlin, Germany", "New York, US" and so on. If you would like the get all the cells describing books published in Norway this would be pretty frustrating thing to do, but with Python we can easily fix this:

First we simply copy-paste the whole sheet to a text editor and save the file. Then in python:

         





### Indentation / Blocks of code

With the conditional statements (if & else) and iterations (for -loops) we encountered indented code. An example from last part would looked like this:

```python
ages = []
for member in member_registry:
    birth_date = member["birth_date"]
    age = date(1944, 9, 19) - date(birth_date)
    ages.append(age)
```

Everything indented together on the same level of indentation constitutes a _code block_, that is to say, a series of commands grouped together. The block starts with a line ending with colon `:`, which is typically a conditional statement, loop or a function definition (more on those next). The block ends when there's a line that is not indented. Like this:   

```python
ages = []
for member in member_registry:
    birth_date = member["birth_date"]
    age = date(1944, 9, 19) - date(birth_date)
    ages.append(age)
print(ages)
```

Lines from `birth_date ...` to `ages.append(age)`are part of the code block insode the for -loop. The final `print(ages)` -command is not part of the block.

A code block can be inside another code block, like we saw in the last examples of the previous part:

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]

for birth_year in birth_years:
    age = 1944 - birth_year
    if age > 17:
        print("Adult")
    else:
        print("Minor")
```

Above, the code block holding the contents of the for-loop also has two smaller 1-line blocks inside it: the `print("Adult")` and the `print("Minor")` blocks are contained within the block for the loop.

Think of _code blocks_ as small semi-independent sections of code that have their own small task to perform.  

### Functions

We have been using _functions_ a lot already. Almost every command we've employed so far, from `print()` to `len()` and `quit()` are functions. A function is basically a simple independent program with its own input and output. A function's input are the paramenters that are given to it inside the parenthesis following its name. For example:

```python
print("Some text!")  
```

The `print()` -function above was given a string with the text "Some text!" as an input. The output of that is printing that text in terminal. Another example would be:

```python
string_length = len("Another string of text.")
print(string_length)
```

The function `len()` is given a string as a parameter. That function counts
length of various objects, in this case that string. The output of the function (23) is then stored in the variable `string_length`. That variable is in turn given to the familiar funtion `print()` as an input, and printed out, like we would expect print to do.

#### Defining your own functions

As mentioned before, the benefit of writing a program to do some task is that we can automate a repeating task. That holds for parts of those programs too. Say, of we wanted to take the previous birthyear- example and test for the adulthood/minority for a variety of years in time, we would end up writing the same code multiple times. A solution is to write a function of our own: We want to create a single command that is given a birthyear and a historic year as parameters, and that tells us if that person was an adult or not on that specific year. So, let's do that:

```python
def is_adult(birthyear, historic_year):
    if historic_year - birthyear > 17:
        return(True)
    else:
        return(False) 
```

So, what happens in the above code? We start with a line that tells Python that we are defining a function. That's the `def` -command there. Then we give the name of the function that we are creatign `is_adult`, and the parameters that it accepts: `(birthyear, historic_year)`. We finish with `:` to tell Python that we are starting a code block whit the actual things that the function does.

Within the function we compare the two variables that are given to it as parameters, and with the `return()` command tell what the output will be. So, if the age of the person on the given year is greater than 17, our function returns the value `True`, and otherwise it returns the value `False`.

We would use our function in our own script like this:

```python
birthyear_aino = 1922
birthyear_maija = 1933
year = 1945

# The following places True in is_adult_aino 
# functions are given the parameters in the same order as
# they were in the definion.
is_adult_aino = is_adult(birthyear_aino, year)
# let's print that too ...
print(is_adult_aino)

# And this one is False ...
# alternatively you can give parameters by specifying their names
# when calling the function. In that case, the order does not matter
is_adult_maija = is_adult(historic_year=year, bithyear=birthyear_maija)
print(is_adult_maija)
```

### Iterations II

Antti
for loop over range(0, whatever)

### String manipulation

Antti
finding, slicing, splitting, joining, stripping certain characters

### Libraries

importing
