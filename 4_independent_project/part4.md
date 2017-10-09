# Independent coding project, part I

This and the next lesson give general instructions for steps to complete a small coding project on your own. The end result of this project will be a Markov-chain based text generator. The basic idea is to take a source text (for example the Idiot by Dostoyevsky), create a "database" based on that text, and use that data to generate random sequences of text that will be original, but in the style of our source.

Internet is full of examples of Markov-chains used to generate text. A good example, built around tweets by Donald Trump laying out the logic behind the construction of these chains can be found [here](https://filiph.github.io/markov/).

During part I we'll create the data that we build the Markov chains from, and in part II we will create the actual chains.

To be able to create the Markov-chains, we will need a database that has every single word occurring in the text, paired with the words immediately following it. So, for example, take the word "Muishkin" (name of a character in the text). We'll want to know how probably it is followed by "was", "did", "suddenly", etc. and so on for all the possible word combinations. In other words, we'll be creating a statistical overview of all the bigrams ([what were n-grams again?](http://text-analytics101.rxnlp.com/2014/11/what-are-n-grams.html)) in the text.

There will be no instructions on code syntax this time. Refer back to previous lessons for that. You'll find it easier to do the below in parts, and trying to print out the variables to make sure you are on the right track. You might also want to try out your code in the interactive Python shell.

## Goals for part I

In this part we'll:

* Read the text into Python.
* Break the text down to bigrams.
* Create a statistical overview of said bigrams.

After finishing the above steps, we are ready to create the Markov-chain text generator in part II.

## Setting up

Start by creating a new project directory and inside that a new python script file for your code. Find a source text from [Project Gutenberg](https://www.gutenberg.org/catalog/) to use in the project.

* Create a new directory for the project.
* Create a new script file in that directory.
* Copy a source text file (.txt) into that directory.
* Clean the source text file of the header and footer -parts added by Project Gutenberg.

## Read source text

We need some way to read the textfile that we are about to use as our source into Python. Like previously, we'll import those from a ready made module, and use the imported functions to read the source file.

* Copy [textfile_io.py](https://raw.githubusercontent.com/COMHIS/python-basics/master/4_independent_project/textfile_io.py) to your project directory.
* _[Import the function](../3_basic_concepts_ii/importing.md)_ for reading text files to strings.
* Use the imported function to save the text into a string variable.

## Creating bigrams

Chop the text string into a list of single words, and then find all the bigram pairs for that word. Save this all in a big dictionary.

You'll want to first split the string into a list, then find all unique words in it by creating a set from it. Then you are ready to create your dictionary: The unique words are the keys, and each key has a list of words following it as its value. You need to first create a dictionary with the keys pointing to empty list, to have something that you can add to later. Then you will need to iterate through each word in the list of words and add the word following that to the corresponding list in your dictionary.

* Make a _list_ of words out of your string with the source text.
* Create a _[set](../3_basic_concepts_ii/lists.md)_ from the list
* Create a _[dictionary](../3_basic_concepts_ii/lists.md)_ with the values in the set as keys, and empty list as the value     stored at each key. (See tips below.)
* Iterate through all the words in the big list of words by index
  * Get the word at the index (first half of bigram)
  * Get the word at the next index (second half of bigram)
  * Add that second half of the bigram to a list at your dictionary at a key corresponding with the first half

### Additional tips:

* How do you create the dictionary with empty lists? Do this by iterating through the values in the _set_, and add each of those values to the dictionary as a key, with an empty list (`[]`) as its value pair. See [this bit in lesson 3](../3_basic_concepts_ii/lists.md) for further details.
* Remember how to access list items by index? [This is just that all the way](../3_basic_concepts_ii/lists.md)
* Iterate with the `for i in range(start, end)` [-loop](../3_basic_concepts_ii/iterations2.md).
* The first half of the bigram can be accessed with `wordlist[i]`
* The second half of the bigram can be accessed with `wordlist[i + 1]`

## Done!

We're ready to go to the next part now. But if you want, you can create statistics for the bigrams to get a better overview of our material.

Iterate through each key in the dictionary and count the words in the list stored at each key. Create a new dictionary to store your results at, and see how it looks.

You should end up with something like this:

```python
>>> all_counts['Alexey']
{'counts': {'Karamazov,”': 1, 'Fyodorovitch....': 1, 'Fyodorovitch,': 54, 'Fyodorovitch,”': 7, 'Ivanitch.”': 1, 'Karamazov—there’s': 1, 'Fyodorovitch.': 11, 'would': 1, 'Fyodorovitch!”': 1, 'Fyodorovitch—to': 1, 'Fyodorovitch?': 2, 'Fyodorovitch—be': 1, 'Fyodorovitch.”': 5, 'Fyodorovitch!': 5, 'more': 1, 'Fyodorovitch;': 3, 'Ivanitch': 1, 'I': 1, 'Fyodorovitch’s': 2, 'Fyodorovitch': 11, 'Karamazov': 2, 'Fyodorovitch?”': 3, 'Karamazov,': 1, 'was': 1}}```
