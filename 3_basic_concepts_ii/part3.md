# Part 3 - Basic concepts in programming II

This part will familiarize you with the second group of basic concepts. After understanding these, you are in theory ready to go. There is still a lot of ground to cover beyond these concepts, but for an aspiring digital humanist, you are basically ready to go.

## Important reminder

The basic logic of programming applies again. Input-> blahblah-> output

---

## Concepts to be covered

In the following we'll cover:

* [**Lists and dictionaries**](./lists.md) - two data types that are extremely useful in storing data within a script
* [**Indentations / Code blocks**](./codeblocks.md) - the way to create subsections in script
* [**Functions**](./functions.md) - small mini programs inside our script files
* **Manipulating strings** - manipulating and modifying text variables
* Some more things on **Iteration** - loops continued
* [**Importing modules**](./importing.md) - many useful commands are not included in the basic group included with Python, and need to be added separately.

---

### Overview

We'll go thought these concepts by going back to our [Dostoyevsky example](../2_basic_concepts/suddenly.md) from the previous part. Instead of looking at the concordance lines with 'suddenly' we'll now dig out so called [2-grams](http://text-analytics101.rxnlp.com/2014/11/what-are-n-grams.html), that is to say, the text split into 2 word sequences.

First, have a look at the code as it is, to get a general overview of it. No need to understand everything just yet:

[dostoyevsky_2grams.py](./dostoyevsky_2grams.py)

To get a feel of where are we heading try running the code also. We're applying the methods to another source text now, namely "The Brothers Karamazov". Do as you did previously, and save [intros.py](https://raw.githubusercontent.com/COMHIS/python-basics/master/3_basic_concepts_ii/intros.py) and [dostoyevsky_concordance.py](https://raw.githubusercontent.com/COMHIS/python-basics/master/3_basic_concepts_ii/dostoyevsky_2grams.py) into a new directory, and use python to run `dostoyevsky_2grams.py`.


Now, lets break to code down, a section at a time, and have a look at what is going on. Look at the code first, read the immediate explanation and go through the link to get a hopefully more clear and thorough breakdown of what is going on.

---

### Importing

At the very top, we import some functions and modules that we will be using later in the code: 

```python
from intros import (read_txt_file_to_list,
                    write_dict_to_csvfile)
import string
```

**Read more:** [Importing modules and functions](./modules.md)

---

### Variables 

After that, we define a few variables that we'll use for our input data and the term that we are going to construct the 2-grams around:

```python
inputfile = "brothers_karamazov.txt"
search_term = 'suddenly'
```

Refer back to [Part 2](../2_basic_concepts/part2.md) for explanation on variables, if you need to.

---

### Functions and code blocks

Next, we'll create a function to help us with changing our to data to conform with what we need for constructing our 2-grams.

```python
def strip_punctuation(text):
    # strip out all punctuation characters
    exclude_characters = set(string.punctuation)
    # some add additional characters we want to strip
    exclude_characters = exclude_characters.union(set("“”"))
    for character in exclude_characters:
        text = text.replace(character, "")
    return text
```

In the function we use the `string` -module we imported earlier, to get a ready list of punctuation characters. We will use the function we have defined soon.

**Read more:** [Code blocks (or indentation)](./codeblocks.md)

**Read more:** [Functions](./functions.md)

---

### Lists

Then, we'll prepare our data and modify it to fit into the kind of Python data structures that we need for our analysis steps.

First, read the text source file and make a _list_ of lines using the function we imported at the start of the script.

```python
# Read text file into a list
lines = read_txt_file_to_list(inputfile)
```

Then we'll use a function called `.join()` to combine those lines into one long _string_. The `''` at the start means that the lines are joined by an _empty string_ - meaning that we add nothing between each line. If we had `'  '` there, we'd add two spaces between each line, etc.

```python
# Join all the separate lines of text into one string
text_combined = ''.join(lines)
```

We are not interested in capitalization, and want to match both upper and lower case words, so we make everything lowercase.

```python
# make everything lowercase
text_combined = text_combined.lower()
```

We'll use the function that we defined earlier to remove punctuation characters (such as: , . ! ? etc.) from the text. We really are interested in the actual words only this time. 

```python
# strip punctuation
text_combined = strip_punctuation(text_combined)
```

Next, being happy with how we've modified the text, we will break it down to a list. Our list will be all the words of the book, in sequence and  changed to lower case. A section of it looks like this: `['are', 'shrewd', 'and', 'intelligent', 'enough—but', 'just', 'senselessness', 'and', 'a', 'peculiar', 'national', 'form', 'of', 'it', 'he', 'was', 'married', 'twice', 'and', 'had']`

```python
# Create text tokens - that is, a list of all the words in th text
text_tokens = text_combined.split()
```

We'll also create an empty list to hold our results. We'll soon add to it using the `.append()` -function.

```python
# create an empty list
tokens_with_search_term_preceding = []
```

**Read more:** [Lists (and dictionaries)](./lists.md)
**Read more:** [String manipulation](./string_manipulation.md)

---

### Iterations

Next we'll consider each token (word in our long list of words) and add it to our list of results, if it satisfies our condition. We'll use a bit different form of _for-loop_ here than previously. We'll also use list slicing and index to get the 2-grams out from our list of words. 

```python
for i in range(0, len(text_tokens) - 2):
    tokenpair = text_tokens[i:i + 2]
    if search_term == tokenpair[0]:
        tokens_with_search_term_preceding.append(tokenpair[1])
```

The row `tokenpair = text_tokens[i:i + 2]` might warrant further explanation: We use the index `i` that we get from our _for-loop_ to access elements in the list of words for the text. So, text_tokens[1010] would be word number 1010 in that list, etc. List slicing is explained in the section about lists, but because of how it works (the format is: `first_item_to_include:last_item_not_included)` to get a two-word sequence (that is, a 2-gram), we need to give the slicing command the index where we want to start at, and the index that is two greater. So, for example `text_tokens[1010:1012]` does produce the 2-word list `['just', 'senselessness']`.

**Read more:** [Lists, and slicing them](./lists.md)
**Read more:** [Iterations II](./iterations2.md)

---

### Sets and dictionaries

Now we have a list of the words that create a 2-gram pair with 'suddenly', but that list is a mess. It's just an unordered list of words. We'll want to count how many times each word is in that list to get some actual sensible results out. 

First, we'll find all the unique words in that list (unique meaning here that we'll count "him", "it", or any other word only once, even if it occurs multiple times). Next we'll create an empty dictionary to hold our results.

```python
# find unique terms in our group of terms:
tokens_set = set(tokens_with_search_term_preceding)
token_counts_dict = {}
```

Next we'll loop over all the unique terms that in the _set_ that we just created, and count the number of times that term appears in our list of terms paired with 'suddenly' in 2-grams. Those terms are held in the list `tokens_with_search_term_preceding`, and counting elements in a list is easy with the `.count()` -function. (In general in programming, you don't remember every command by heart. Instead you google what you want to do: [Like this!](https://www.google.fi/search?&q=how+to+count+items+in+list+in+python&oq=how+to+count+items+in+list+in+python))

Finally, we place the value under a key with the term name in our dictionary of results.

```python
# count the number of occurrences for each item in set
for token in tokens_set:
    occurrences = tokens_with_search_term_preceding.count(token)
    token_counts_dict[token] = occurrences
```

**Read more:** [This kind of for-loops were covered last time](../2_basic_concepts/part2.md)
**Read more:** [Lists, dictionaries and sets](./lists.md)

---

### Writing our results

At the end of our script, we have to save our results somewhere. We'll go with .csv -file, the standard format for spreadsheet -like data. We'll use the function we imported at the start of our script to do this. Have a look inside [intros.py](./intros.py) to see what that function actually does.

```python
outputfile = "suddenly_2grams.csv"
write_dict_to_csvfile(token_counts_dict, outputfile)
```
