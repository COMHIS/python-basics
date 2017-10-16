# Independent coding project (markov-chains), part II

We'll continue from where we finished at [part 4](../4_independent_project/part4.md), so everything you are instructed to do here, add to the end of that script.

The aim now is to use the dictionary of bigram pairs we created to construct a random text in the style of the original, in other words, a markov-chain text generator.

## Inpecting what was done

As a first step, let's remind ourselves of what we actually did, and make sure our data is good. There's a way to run a Python script, and then leave Python running. This will let us inspect the values in the variables in our script. Run the script you created previously by adding the `-i`-command line option. Like so: `python3 -i nameofyourscript.py`.

Your script will run and you'll end up in the interactive Python shell. Now, inspect the dictionary where you saved your bigram lists. Your dictionary should have a structure where all the first halves of the bigrams are keys, and the corresponding second halves are stored in a list under that key.

Use the interactive shell to list all the keys in the dictionary. Try [googling](https://www.google.fi/search?safe=off&q=python+dictionary+keys&oq=python+dictionary+keys) how to do that. Remember, programming is at least 50% googling!

Choose a key from the list you printed and get the value (list of words) associated with that key. Remember the `.get()` -method of dictionaries? Now take on of the words on the list you just printed and use it to get another list, and so on. The process might look something like this:

```python
# get words for 'drawn':
>>> the_command_that_does_that('drawn')
['him', 'to', 'by', 'down', 'to', 'by', 'out', 'your', 'to', 'to', 'out,', 'into', 'by', 'up,', 'up', 'by', 'by', 'by', 'from', 'with', 'smile,']

# choose one of those, say 'into'
>>> the_command_that_does_that('into')
... 'psychological', 'which', 'the', 'romancing,', 'a', 'the', 'the', 'that', 'prison.', 'silence', 'the', 'a', 'his', 'the', 'a', 'a', 'the', 'a', 'negotiations....', 'a', 'the', 'tears.', 'the', 'everything.”', 'his', 'his', 'the', 'the', 'loud', 'rapid,', 'brooding', 'sobs.', 'his', 'great', 'life,']

# choose one of those, say 'psyhological'
>>> the_command_that_does_that('psyhological')
['process.', 'Ippolit', 'case', 'subtleties', 'insight.', 'insight', 'subtlety,', 'method']
```

## Aim for today

Next, we'll want to automate what we just did. Our code will create a text of a set length, with a similar method as we did manually above. The steps are, briefly:

* Start with the dictionary you created before (= continue below your previous code)
* Create a variable that give the length of the text you want to generate in words.
* Set a word to start the generator with.
* Create a loop in which you choose a random word paired with the word above, and repeate that with the previous word until you have created a long enough text.

## Steps in detail

### Some variables to start with

First, create the variables needed for the loop (and set their values):

* Length of the text to be generated in words.
* The starting word.
* List to store the generated text in (with the starting word in it).

### Start of the loop

Create a loop that repeates as many time as you set the length of the text to be generated to. There are multiple ways to do this, but the one we've learned is the `for i in range(0, how_ever_many):` -method. _If_ you feel adventurous, you can [google python while -loops](https://www.google.fi/search?q=python+while+loops).

* Loop looping as many time as we want to generate words.

### Contents of the loop

Each time we add a word into the generated text we need to find the last word in it. As our text is stored in a list, this is as simple as accessing the last element of the list. Refer back to the [section on lists](../3_basic_concepts_ii/lists.md), or [google](https://www.google.fi/search?safe=off&q=python+last+element+of+list) on how to do it. Store that in a variable at the very start of the loop.

* Variable pointing to the last element of the words generated -list.

Then get the list of words associated with the word we fetched above, and store that in another variable. Do this exactly as you did previously when manually testing the process, but this time use the variable where we stored the last word in the results list as a key.

* Get the list of bigram pairs associated with the last word.
* ... and store it in another variable.

### Contents continued- random word from the list

Continue with the loop still:

Now comes the magical part! We'll choose a word at random from that list of bigram pairs. We've used random previously in a [few](../3_basic_concepts_ii/importing.md) [places](../3_basic_concepts_ii/iterations2.md). You need to add a line to the very start of your script to import the `randint`-function from the module `random`.

* Import randint from random.

Next, you need to generate a number that will be used as an index for accessing a word from the list of bigram pairs. The first index in any list is 0, and the last one is the length of the list minus one (Remember, things in python are 0-indexed, that is a list of 3 items would have indices 0, 1 and 2.). `randint` takes two parameters, which give the range of integer to choose from. So, for example, `randint(0,9)` chooses, at random any integer from 0 to 9.

Place that random number in a variable, and retrieve the word in the list of bigram pairs corresponding to the randomly chosen index.

* Choose a random word from the list of bigram pairs.

Still within the loop, add that randomly chosen word to the end of our results list.
**Tip:** Remember the `.append()` -method here.

### Finishing touches

We should be almost done now. The results list should have randomly chosen words in sequence, with a semisensible structure. Join that list into a string, and write it into an output file. After that you're done! After a succesful run try alterin the length parameter.

Combining the list to a single string is easy. Just [google](https://www.google.fi/search?q=python+combine+list+into+string) it. This too should be stored in a variable. In general you want to be storing things in variables all the time.

The `textfile_io.py` -module has a function (a bit confusingly by the name `write_txt_file_to_string`. A newer version has the function renamed to a more sensible `write_string_to_txt_file`) for writing string to text file. Import that a the start of the script and use it to save the string into a text file. 

**You're done!** Inspect the output file, and decide if it makes sense or not.

---

### Bonus assignment

**Only do these if you feel you need an extra challenge!**

* Instead of an output with a set number of words, try generating one complete sentence. 
* Bigrams create pretty nonsensical text. Try altering the code to create the markov chains with trigrams instead.
