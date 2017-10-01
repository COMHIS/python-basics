# Part 3 - Basic concepts in programming II

This part will familiarize you with the second group of basic concepts. After understanding these, you are in theory ready to go. There is still a lot of ground to cover beyond these concepts, but for an aspiring digital humanist, you are basically ready to go.

---

## Concepts to be covered

In the following we'll cover:

* **Lists and dictionaries** - two datatypes that are extremely useful in storing data within a script
* **Indentations / Code blocks** - the way to create subsections in script
* **Functions** - small miniprograms inside our script files
* **Manipulating strings** - manipulating and modifying text variables
* Some more things on **Iteration** - loops continued
* Importing **modules** - many useful commands are not included in the basic group included with Python, and need to be added separately.

---

### Lists and dictionaries

The reason why programming is such a useful thing to learn, is that you are very soon able to automatise repetitive tasks. The amount of time you spend writing the code does not depend on the size of your dataset, and for most simpler tasks the computer can run through thousands of rows of data in seconds.

In order to get acquainted with handling datasets and their manipulation, we first take a look at the most common data structures implemented in Python to hold more variables than just one. They are called _lists_, _dictionaries_ and _tuples_.

Basically their idea is the same: you can refer to whole bunch of variables with just one name! Their differences comes from how you operate them and access the variables put into them.

#### List

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
A common problem for any Excel-humanist is that the original data might contain in one column two variables. Imagine that you are researching book history and on one column of your otherwise flawless Excel-sheet you have the publication place written in the form of "City, Country". Like "Antwerpen, Netherlands", "Berlin, Germany", "New York, US" and so on. If you would like the get all the cells describing books published in Norway this would be pretty frustrating thing to do, but with Python we can easily fix this by following the steps:

1) copy-paste Excel sheet into a text editor and save it as a .tsv -format file
2) read the file in python as list of rows
3) iterate over the list and use split-function to split each row into a list with using tab ("\t") as a separator
4) now we have the excel sheet as list of lists where each row is represented as a list, in turn containing a list of strings corresponding to columns. We could now access any any cell in the sheet by its coordinates: sheet[3][4] would return the value in the 5th column of the 4th row.
5) the we will iterate over the rows and use replace()-function to change comma (",") to a tab ("\t") in the "publisher"-field we wanted to split and join the row back to a single string with join()-function.
6) now when we join() the rows back together and write the result to a file. When we open the tsv-file in text editor, we can then copy-paste it back to Excel.

Lists are mutable which means that they can be changed on the go. You can add more elements to a list or remove them. You can count how many times a specific element occurs in the list or sort a list based on whichever criteria you see fit. And so on.

**Dictionaries**

Dictionaries can be thought like a special type of list, where items in the list are not accessed by indices but by specific _keys_. Key is a name given to a specific value.

```python
my_dict = {"name":"Introduction to Digital Humanities", "points": 5, "year":2017}
```
Like with lists, you can add any kinds of data to a dictionary. Keys must always be strings or integers, but values may be other dictionaries or lists or nested combinations of these.

Accessing dictionary items by key is done like this:

```python
print(my_dict["name"])
Introduction to  Digital Humanities
```
 
If you want to add a new key-value pair to a dictionary, you can simply assign the key or use update()-function:

```python
my_dict["semester"] = "Autumn"
my_dict.update({"start_date":"1.9.2017"})
print(my_dict)
my_dict = {"name":"Introduction to Digital Humanities", "points": 5, "year":2017, "semester":Autumn, "start_date":"1.9.2017"}
```

A very common computational / corpus linguistic task is to compile a word frequency list out of large text. It is easy to do using a dictionary:

```python
text=open_text_data("dostoyevsky.txt") #let's presume we have a custom function 
                                        that open the Dostoyevsky text file for 
                                        us as a large string obejct called 'text'
                                        
text = text.split(" ")                 #here we split the text in to a list of words

word_frequencies = {}                  #let's create an empty dictionary

for word in text:                      #while iterating the text as a list of words
    if word not in word_frequencies:   #if we encounter a new word, we assign a key for it
        word_frequencies[word] = 1      in the dictionary with value 1 (as this is the first time
                                        this word is seen)
        
    else:                              #if the word already is as a key in the dictionary,
        word_frequencies[word] += 1    #we just add one to the existing value
```
                                        
**Tuples**

Tuples are the third built-in list like data structure in Python. Tuples are pretty much like list, but they are _inmutable_, which means they cannot be altered after being created. No new items can be added to or removed from them, their order can not be changed et cetera. That's about it, enough said.

Very seldom you need tuples for anything. Tuples are faster that lists and take less space in the memory, but you have to deal with quite big datasets before this becomes an issue. If you use functions from libraries made by someone else, they sometimes return the result as a tuple so it is good to know what they are.

A tuple is created using normal brackets:

```python
my_tuple = ("IF Gnistan", 1924, "Oulunkylä", "Åggelby")
```

**JSON and Complicated Data Structures**

It is common for example APIs or syntactic or morphological parser to return the data they have provided for you in so-called JSON-format. JSON data structures are practically identical to Python data strcutures and the notation is the same. So if you, for example, use the KORP corpus interfaces API, it will return something like this:

```json
{
"progress_corpora": ["KLK_FI_1878", "KLK_FI_1879"],
"progress_0": {"corpus": "KLK_FI_1878", "hits": 6},
"progress_1": {"corpus": "KLK_FI_1879", "hits": 19},
"hits":133,"kwic":[{"tokens":[{"ocr":"0.94","word":"Kulkiivat","lemmacomp":"Kulkiivat","pos":"N","nertag":"_","lemma":"Kulkiivat","dephead":"6","nerbio":"O","lex":"|Kulkiivat..nn.1|","msd":"NUM_Pl|CASE_Nom|CASECHANGE_Up|OTHER_UNK","ref":"1","structs":{"open":["sentence"]},"deprel":"nsubj"},{"ocr":"0.93","word":"vaiva","lemmacomp":"vaiva","pos":"N","nertag":"_","lemma":"vaiva","dephead":"1","nerbio":"O","lex":"|vaiva..nn.1|","msd":"NUM_Sg|CASE_Nom","ref":"2","deprel":"nommod"},{"ocr":"0.99","word":"(","lemmacomp":"(","pos":"Punct","nertag":"_","lemma":"(","dephead":"4","nerbio":"O","lex":"|(..xx.1|","msd":"_","ref":"3","deprel":"punct"},{"ocr":"0.99","word":"K.","lemmacomp":"K.","pos":"N","nertag":"_","lemma":"K.","dephead":"2","nerbio":"O","lex":"|K...nn.1|","msd":"SUBCAT_Abbr|CASECHANGE_Up|OTHER_UNK","ref":"4","deprel":"appos"},{"ocr":"0.99","word":")","lemmacomp":")","pos":"Punct","nertag":"_","lemma":")","dephead":"4","nerbio":"O","lex":"|)..xx.1|","msd":"_","ref":"5","deprel":"punct"},{"ocr":"0.99","word":"kulkivat","lemmacomp":"kulkea","pos":"V","nertag":"_","lemma":"kulkea","dephead":"0","nerbio":"O","lex":"|kulkea..vb.1|","msd":"PRS_Pl3|VOICE_Act|TENSE_Prt|MOOD_Ind","ref":"6","deprel":"ROOT"},{"ocr":"0.99","word":"vaivoin","lemmacomp":"vaiva","pos":"N","nertag":"_","lemma":"vaiva","dephead":"6","nerbio":"O","lex":"|vaiva..nn.1|","msd":"NUM_Pl|CASE_Ins","ref":"7","deprel":"nommod"},{"ocr":"0.96","word":"t.","lemmacomp":"t.","pos":"Num","nertag":"_","lemma":"t.","dephead":"6","nerbio":"O","lex":"|t...rg.1|","msd":"OTHER_UNK","ref":"8","deprel":"nommod"},{"ocr":"0.99","word":"suurella","lemmacomp":"suuri","pos":"A","nertag":"_","lemma":"suuri","dephead":"10","nerbio":"O","lex":"|suuri..jj.1|","msd":"NUM_Sg|CASE_Ade|CMP_Pos","ref":"9","deprel":"amod"},{"ocr":"0.99","word":"vaivalla","lemmacomp":"vaiva","pos":"N","nertag":"_","lemma":"vaiva","dephead":"6","nerbio":"O","lex":"|vaiva..nn.1|","msd":"NUM_Sg|CASE_Ade","ref":"10","deprel":"nommod"},{"ocr":"0.99","word":".","lemmacomp":".","pos":"Punct","nertag":"_","lemma":".","dephead":"6","nerbio":"O","lex":"|...xx.1|","msd":"_","ref":"11","structs":{"close":["sentence","paragraph"]},"deprel":"punct"}],"corpus":"KLK_FI_1879","structs":{"text_issue_no":"13","text_publ_title":"Suomi","paragraph_id":"2","text_issue_title":"SUOMI","sentence_local_id":"8","text_sentcount":"23","text_language":"fi","text_issue_date":"1879","text_img_url":"#DIRECTORY#0355-0257_1879_13#SEPARATOR#00063.#EXTENSION#","text_label":"SUOMI no. 13 1879","sentence_id":"1318","text_publ_id":"0355-0257","text_publ_type":"aikakausi","sentence_parse_state":"parsed","text_binding_id":"498462","text_tokencount":"345","text_elec_date":"2007-03-27","text_page_no":"63"},"match":{"position":16870,"end":2,"start":1}},{"tokens":[{"ocr":"0.82","word":"Waiwais","lemmacomp":"Waiwais","pos":"N","nertag":"_","lemma":"Waiwais","dephead":"0","nerbio":"O","lex":"|Waiwais..nn.1|","msd":"SUBCAT_Prop|NUM_Sg|CASE_Nom|CASECHANGE_Up|OTHER_UNK","ref":"1","structs":{"open":["sentence"]},"deprel":"ROOT"},{"ocr":"0.82","word":"\u00bb","lemmacomp":"\u00bb","pos":"Punct","nertag":"_","lemma":"\u00bb","dephead":"1","nerbio":"O","lex":"|\u00bb..xx.1|","msd":"_","ref":"2","deprel":"punct"},{"ocr":"0.93","word":"ja","lemmacomp":"ja","pos":"C","nertag":"_","lemma":"ja","dephead":"1","nerbio":"O","lex":"|ja..kn.1|","msd":"SUBCAT_CC","ref":"3","deprel":"cc"},{"ocr":"0.88","word":"Ty\u00f6huonerahasto","lemmacomp":"ty\u00f6huone|rahasto","pos":"N","nertag":"EnamexOrgCrp/","lemma":"ty\u00f6huonerahasto","dephead":"1","nerbio":"B","lex":"|ty\u00f6huonerahasto..nn.1|","msd":"NUM_Sg|CASE_Nom|CASECHANGE_Up","ref":"4","structs":{"close":["ne_placename_source","ne_placename","ne_subtype","ne_type","ne_ex","ne_fulltype","ne_name"],"open":["ne_name Ty\u00f6huonerahasto","ne_fulltype EnamexOrgCrp","ne_ex ENAMEX","ne_type ORG","ne_subtype CRP","ne_placename ","ne_placename_source "]},"deprel":"conj"},
```



---

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

---

### Functions<a name="intro_functions"></a>

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
        return True
    else:
        return False 
```

So, what happens in the above code? We start with a line that tells Python that we are defining a function. That's the `def` -command there. Then we give the name of the function that we are creatign `is_adult`, and the parameters that it accepts: `(birthyear, historic_year)`. We finish with `:` to tell Python that we are starting a code block whit the actual things that the function does.

Within the function we compare the two variables that are given to it as parameters, and with the `return()` command tell what the output will be. So, if the age of the person on the given year is greater than 17, our function returns the value `True`, and otherwise it returns the value `False`.

We would use our function in our script like this:

```python
def is_adult(birthyear, historic_year):
    if historic_year - birthyear > 17:
        return True
    else:
        return False 


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
---

### Iterations II

Antti
for loop over range(0, whatever)

---

### String manipulation

Antti
finding, slicing, splitting, joining, stripping certain characters

---

### Modules

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
