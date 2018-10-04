# Anthropomorphism in the Jungle Books

This assignment has three parts:

1) make a script that can find all (or most of ;) the characters in the Jungle Books.
2) make a script that can produce a concordance list of any character's name's occurrences in the text.
3) analyse one or compare two (or more) characters by some features of their textual environments, either by tagging manually or automated processing.

Such as: "who speaks more, Ka or Baloo?"
or: "what does Mowgli mostly do in the text? Which other character also engages in similar activities frequently?"
or: "which characters are mentioned together most often?"

## Getting the data

The raw text versions of the Jungle Book and the Second Jungle Book can be found in the Project Gutenberg website: www.gutenberg.org.
Navigate the site to find the two files.

Famialiarise yourself little with the data. How is it composed? Where is the actual text?

## Start coding! (But plan each step first)

If you feel lost, ask for help.

### Step 1: Read the data into a list of lines of text.

There are suitable resources available in previous excercises (intros.py)
Iterate through the lines and split the each line into a list of words using split() function.

```python
string.split(" ") 
```

splits a string by every blank space.

For example:
```python
"a string by every blank space".split(" ") 
```
would return:
```python
["a", "string", "by", "every", "space"]
```
### Step 2: Find all of the words that start with a capital letter and count their frequencies. 

In python, you can ask from a string whether it is in all capital or lower letters.
```python
string.islower() 
```
is True if all of the letters in the string are lower case,
```python
string.isupper() 
```
is True if all of the letter in the string are upper case.

Hint: Good way to counting is using a dictionary. Every time a counted item is found while iterating, add 1 to its value.

To get the most frequent words, this dictionary has to be somehow ordered by the values.
However, dictionary has no order. What to do? How to sort this kind of dictionary? Impossible!

Hint: Try googling "python sorting dictionary by value"...

Using the frequencies of the words, select from the most frequent capital words those that are names of characters.

### Step 3: Concordance list
Easy way to make concordance list is to simply add "\t" character on each side of the word that is to be highlighted. When the line is printed out, it can be copy-pasted to excel or google sheets for easy browsing.

### Step 4: Research!

Think for a nice compact research question and try to answer it using for example the concordance lists. Sometimes best way to tackle a problem is manual inspection and tagging, sometimes automated processing.
