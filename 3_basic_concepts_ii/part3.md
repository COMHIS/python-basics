# Part 3 - Basic concepts in programming II

This part will familiarize you with the second group of basic concepts. After understanding these, you are in theory ready to go. There is still a lot of ground to cover beyond these concepts, but for an aspiring digital humanist, you are basically ready to go.

---

## Concepts to be covered

In the following we'll cover:

* [**Lists and dictionaries**](./lists.md) - two datatypes that are extremely useful in storing data within a script
* [**Indentations / Code blocks**](./codeblocks.md) - the way to create subsections in script
* [**Functions**](./functions.md) - small miniprograms inside our script files
* **Manipulating strings** - manipulating and modifying text variables
* Some more things on **Iteration** - loops continued
* Importing **modules** - many useful commands are not included in the basic group included with Python, and need to be added separately.

---

We'll go thought thse concepts by going back to our [Dostojevsky example](../2_basic_concepts/suddenly.md) from the previous part. Instead of looking at the concordance lines with 'suddenly' we'll now dig out so called [2-grams](http://text-analytics101.rxnlp.com/2014/11/what-are-n-grams.html), that is to say, the text split into 2 word sequences.

First, have a look at the code as it is, to get a general overview of it. No need to understand everything just yet:

[dostoyevsky_2grams.py](./dostoyevsky_2grams.py)

---

Now, lets break to code down, a section at a time, and have a look at what is going on.


### Importing

At the very top, we import some functions and modules that we will be using later in the code: 

```python
from intros import (read_txt_file_to_list,
                    write_dict_to_csvfile)
import string
```

**Read more:** [Importing modules and functions](./modules.md)

### Variables 

After that, we define a few variables that we'll use for our inputdata and the term that we are going to construct the 2-grams around:

```python
inputfile = "brothers_karamazov.txt"
search_term = 'suddenly'
```

Refer back to [Part 2](../2_basic_concepts/part2.md) for explanation on variables, if you need to.

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

Next, being happy with how we've modified the text, we will break it down to a list. Our list will be all the words of the book, in sequence and  changed to lower case. A section of it looks like this: `['have', 'married', 'such', 'a', 'worthless', 'puny', 'weakling', 'as', 'we', 'all', 'called', 'him', 'i', 'won’t', 'attempt', 'to', 'explain', 'i', 'knew', 'a']`

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


---


---



### Iterations II

Now we can look again the iteration thing, knowing little bit more about the things (list-like-things) we are iterating.

**Iterating lists**

Lists can be iterated in two different ways:
1) running through all the items in a list
2) running through list of numbers as long as the list and using those numbers to access elements with corresponding indices in the list

```python

my_string = "Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice."
my_list = my_string.split(" ")

#method 1: Iterate item by item

for x in my_list:
    if len(x) > 3:
        print(x)
        
Many
years
later
faced
...

#method 2: Iterate indices

for i in range(0,len(my_list)):  #NOTE function range(a,b) returns numbers from a to b-1
    if len(my_list[i]) > 3:
        print(x)
        

Many
years
later
faced
...

```

The main difference between these two is that a list can not be changed while it is being iterated, so we can not remove or add new items to a list with method 1, nor can we change the values in the list.

This restriction is circumvented with method 2, as we are not iterating the list itself, nearly a list of numbers with equal length.

Other reason to use the method 2 would be that it provides a handy way of accessing adjacent items:

```python

for i in range(0, len(my_list)):
    if my_list[i] == "Colonel":
        print(my_list[i-1], my_list[i], my_list[i+1])

squad,   Colonel   Aureliano

```

**Iterating dictionaries**

Like said above, items stored in dictionaries are key-value pairs and the values are accessed by their keys (but not the other way round). And also was mentioned before was that keys are not stored in dictionaries in any specific order. This means that if you iterate the same dictionary many times over during your code, the order might be everytime different, or then it might not.

In practice dictionaries are iterated like this:

```python
my_dict = {"has":34, "is": 59, "a":12}

for key in my_dict:
    print(key)
    if my_dict[key] > 50:
        print("over fifty!")
        
a
is
over fifty!
has
```




---

### String manipulation

The matter of fact is that strings in Python are little more than lists of characters. Almost all operations that can be done on lists, can be done on strings as well. So certain characters in a string can be accessed by its position, string can be sliced by indices. Also lists and strings utilise the '+' sign in similar way:

```python
my_string_A = "Hopefully this"
my_string_B = "is helpful"

my_list_A = ["Hopefully", "this"]
my_list_B = ["is", "helpful"]

print(my_string_A + my_string_B)
"Hopefully thisis helpful"
print(my_list_A + my_list_B)
["Hopefully", "this", "is", "helpful"]
```

---




---

## Excercises

**Note:** As before, each excercise is independent unless otherwise stated, so start each one in a separate script file, or erase old code from the one you use for doing them. Don't paste them all one after the other!

---

### Functions 1

Let's try creating a few functions now. Something really simple as a warmup:

```python
def multiplier(number_a, number_b):
   result = number_a * number_b
   return result
```

We created a function that thakes two numbers, and returns the result of multiplying them. Let's use that function now, and print the results to see what happened:

```python
def multiplier(number_a, number_b):
   result = number_a * number_b
   return result

a = 2
b = 6
result_of_multiplication = multiplier(a, b)
print(result_of_multiplication)
```

Create a similar function now, but for adding two numbers together. Use it and print the results out. 

### Functions 2

Let's go back to our adult/minor exercise, and pack some of the code there into a function. Previously, printing the age group was done like this:

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]

for birth_year in birth_years:
    age = 1944 - birth_year
    if age > 17:
        print("Adult")
    else:
        print("Minor")

```

We'll modify that a bit now and instead create a function that we will call inside the loop. Note that this function doesn't really return anything. It just prints the result:

```python
def print_agegroup(birth_year, historic_year):
    age = historic_year - birth_year
    if age > 17:
        print("Adult")
    else:
        print("Minor")


birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]
historic_year = 1942

for birth_year in birth_years:
    print_agegroup(birth_year, historic_year)
```

Now, modify the function that instead of printing the text "Adult" or "Minor" it will return it as a string. Place that in a variable within the loop and print that variable.

### Functions 3

We've been adding strings together quite a few times previously. As you remember, that went like this: `combined_string = "Digital Humanities" + " is " + "great!".` Let's do that in a function now.

```python
# We'll define a function that takes a string, and returns
# that same string with " the cat" added 
def get_cat_name(name):
    cat_name = name + " the cat"
    return cat_name

# and to use that function:
name1 = "Catty"
name1_catted = get_cat_name(name1)
# and print the catname:
print(name1_catted)

# we can do that inside the print -function too:
print(get_cat_name("Meow"))

# and we can also loop that over a list:
names = ["Joe", "Milly", "Andrei", "Anja-Riitta", "Musti"]
for name in names:
    print(get_cat_name(name))
```

Do something similar yourself. create a function that makes names into houseplant names, like this- from "Joe" to "Green Joe the houseplant". Create the function, and try it out over a list.
