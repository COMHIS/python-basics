## Lists and dictionaries

The reason why programming is such a useful thing to learn, is that you are very soon able to automatise repetitive tasks. The amount of time you spend writing the code does not depend on the size of your dataset, and for most simpler tasks the computer can run through thousands of rows of data in seconds.

In order to get acquainted with handling datasets and their manipulation, we first take a look at the most common data structures implemented in Python to hold more variables than just one. They are called _lists_, _dictionaries_ and _tuples_.

Basically their idea is the same: you can refer to whole bunch of variables with just one name! Their differences comes from how you operate them and access the variables put into them.

### List

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

Adding elements to a list is done by their `.append()` function. So, to add `"concepts"` -string variable to our `miscellania` -list, we'd do this:

```python
miscellania.append("concepts")
```

### Dictionaries

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
A crucial difference compared to lists is that dictionaries are not in any specific order. We will come back to this later when telling how dictionaries are iterated over.


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

### Sets

A dictionary in Python is a lot like a dictionary in real life: You have one key (entry in a dictionary, "The Enlightenment", for example), and a value corresponding to that key (the text that tells what the Enlightenment was all about). Keys are always unique: You can't have a dictionary with two identical keys, and if you try to add a new entry with the same key you end up overwriting the old one.

There are often situations in which we are interested in knowing the unique values in a given list or group of items. Say we have a list of words with many words occuring multiple times. We'll just want to know all the words occuring in that list and are not interested in how many times they do occur. A set comes handy here, as is very similar to dictionary keys: each value in it is unique:

```python
list_of_words = ["free", "banana", "key", "ambition", "the", "banana", "catacombs", "banana", "the"]
set_of_above_words = set(list_of_words)
print(set_of_above_words)
# {'key', 'free', 'ambition', 'the', 'banana', 'catacombs'}
```

Sets can be added into and removed from, among other things:

```python
set_of_words = {'key', 'free', 'ambition', 'the', 'banana', 'catacombs'}
set_of_words.remove("banana")
set_of_words
# {'key', 'free', 'ambition', 'the', 'catacombs'}
set_of_words.add("mango")
set_of_words
# {'key', 'free', 'ambition', 'the', 'catacombs', 'mango'}
```

### JSON and Complicated Data Structures

It is common for example APIs or syntactic or morphological parser to return the data they have provided for you in so-called JSON-format. JSON data structures are practically identical to Python data strcutures and the notation is the same. So if you, for example, use the KORP corpus interfaces API, it will return something like this:

```json
{
"progress_corpora": ["KLK_FI_1878", "KLK_FI_1879"],
"progress_0": {"corpus": "KLK_FI_1878", "hits": 6},
"progress_1": {"corpus": "KLK_FI_1879", "hits": 19},

  "corpus_hits": {
    "KLK_FI_1870": 14, 
    "KLK_FI_1871": 9, 
    "KLK_FI_1872": 9, 
    "KLK_FI_1873": 13, 
    "KLK_FI_1874": 9, 
    "KLK_FI_1875": 14, 
    "KLK_FI_1876": 23, 
    "KLK_FI_1877": 10, 
    "KLK_FI_1878": 13, 
    "KLK_FI_1879": 19, 
    "REITTIDEMO": 0
  }, 
  "corpus_order": [
    "KLK_FI_1879", 
    "KLK_FI_1878", 
    "KLK_FI_1877", 
    "KLK_FI_1876", 
    "KLK_FI_1875", 
    "KLK_FI_1874", 
    "KLK_FI_1873", 
    "KLK_FI_1872", 
    "KLK_FI_1871", 
    "KLK_FI_1870", 
    "REITTIDEMO"
  ], 
  "hits": 133, 
  "kwic": [
    {
      "corpus": "KLK_FI_1879", 
      "match": {
        "end": 2, 
        "position": 16870, 
        "start": 1
      }, 
      "structs": {
        "paragraph_id": "2", 
        "sentence_id": "1318", 
        "sentence_local_id": "8", 
        "sentence_parse_state": "parsed", 
        "text_binding_id": "498462", 
        "text_elec_date": "2007-03-27", 
        "text_img_url": "#DIRECTORY#0355-0257_1879_13#SEPARATOR#00063.#EXTENSION#", 
        "text_issue_date": "1879", 
        "text_issue_no": "13", 
        "text_issue_title": "SUOMI", 
        "text_label": "SUOMI no. 13 1879", 
        "text_language": "fi", 
        "text_page_no": "63", 
        "text_publ_id": "0355-0257", 
        "text_publ_title": "Suomi", 
        "text_publ_type": "aikakausi", 
        "text_sentcount": "23", 
        "text_tokencount": "345"
      }, 
      "tokens": [
        {
          "dephead": "6", 
          "deprel": "nsubj", 
          "lemma": "Kulkiivat", 
          "lemmacomp": "Kulkiivat", 
          "lex": "|Kulkiivat..nn.1|", 
          "msd": "NUM_Pl|CASE_Nom|CASECHANGE_Up|OTHER_UNK", 
          "nerbio": "O", 
          "nertag": "_", 
          "ocr": "0.94", 
          "pos": "N", 
          "ref": "1", 
          "structs": {
            "open": [
              "sentence"
            ]
          }, 
          "word": "Kulkiivat"
```

In these structures lists and dictionaries typically alternate, so that it can take a while until you make sense of what's what. After that the analysis is usually quite straightforward.

## Exercises

These exercises expect you to add to to previous code, unless otherwise noted. So, after finishing **Lists 1**, keep the code and add the following exercise on lines below that in the same script, etc.

### Lists 1

Create a list of years (integers) with some values in it. Like this:

```python
years = [2000, 2015, 1995, 1985, 1765]
```

Make that list have 10 different years in total and print it.

### Lists 2

Now get the third element of that year-list, place it in a varible and print that variable. Accessing elements in a list was done by their index: `mylist[index_to_get]`.

### Lists 3

Do the same, but get years in indices 1-5. This is called slicing, and done like this: mylist[slice_start_index:first_index_not_included_in_slice]

### Lists 4

Seems that we forgot one more year: 2017. Add that to your list of years (using the `.append()` -function), and print the list to make sure everything worked ok.

### Dictionaries 1

Start a new script file. We'll start with a dictionary with people's names as keys and their birith years as the values stored in the dictionary:

```python
ls_register = {'Jasmiina': 1921, 'Henrietta': 1923, 'Justiina': 1933, 'Anja': 1931, 'Aukustiina': 1911, 'Vilma': 1925, 'Josefiina': 1926, 'Marjatta': 1921}
```

Let's try accessing the values in the dictionary. use the `.get()` function to retrive Anja's age, and print it. The formula for that is: `name_of_my_dictionary.get(key)`, so in this case: `ls_register.get('Anja')`

### Dictionaries 2

Let's try iterating our dictionary now. We can get all the keys in it by .keys() -function. First, just to see what they are, and to make sure everything is working, try printing them like this: `print(ls_register.keys())`

To access the keys one by one, we would iterate trough them in a loop like this:

```python
for key in ls_register.keys():
    # and print them for good measure
    print(key)
```

Now in addition to printing the key, also inside the loop print the value stored in the dictionary with each key. You can do that by giving `key` (the variable name we are iterating in the loop) as parameter to the `.get()` -function.