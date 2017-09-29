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
