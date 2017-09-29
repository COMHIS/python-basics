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

         





### Iterations II

for loop over range(0, whatever)

### String manipulation

finding, slicing, splitting, joining, stripping certain characters

### Functions

doing your own
using ready ones

### Indentation / Blocks of code

inside each other

### Libraries

importing
