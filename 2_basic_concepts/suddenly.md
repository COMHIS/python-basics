# Suddenly in Dostoyevsky

Researchers in Russian literature, have been discussing the surprisingly high frequency of the word _vdrug_ (translating roughly to _suddenly_) in Dostoyevsky's novels. They've been arguing that the unexpected has a central role in Dostoyevsky's works, and many have been counting the uses of the word _vdrug_, to be able to more sharply focus on the nature of that element. We'll do a similar excercise here.

There are structures utilized her that we have not covered yet, and you don't need to worry about those. Your task is to modify the code so that it will produce the expected results. The lines you need to modify are preceded by comments starting with `# MODIFY HERE`.

---

## Counting "suddenly"

We'll expand the script in a few steps. First, let's read the text from a file, and count the lines with the word `suddenly` in them. Safe these script files [intros.py](./intros.py) [dostoyevsky1.py](./dostoyevsky1.py) into a directory on your computer, and modify `dostoyevsky1.py` so that it will run without errors. You will also need to load the source text file [the_idiot.txt](./the_idiot.txt) and save it in that save directory.

You should end up with the text `Total 261 lines with the term "suddenly" found.` printing in terminal.

## "Suddenly" concordance

We want to know in more detail what is happening around "suddenly" in the text. For this we'll employ a linguistic concept called _concordance_, which is explained [here](https://www.nottingham.ac.uk/alzsh3/acvocab/concordances.htm).

Now we also want to save our output, and produce a similar concordance output as in the example in the link. After modifying [dostoyevsky2.py](./dostoyevsky2.py) correctly, you should have a results file with that.

**Bonus assignment:** For those who want to do one. We seem to have produced valid .tsv format there. Find a way to open the output file we produced in a spreadsheet program.


* load a text of dostoevsky's from project gutenberg



## The logic of the program:

* read lines into list
* process elements in list of lines, find word
  * check if word substring in line. 
  * if yes, insert tabs into string


* people associated with
* environment - scenes?
* said by whom?
