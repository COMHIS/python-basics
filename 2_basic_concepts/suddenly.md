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

## "Suddenly" over the whole work

Let's have a more statistical overview of the use of "suddenly" in _the Idiot_ now. We'll want to create a measure to track the "suddenliness" of a limited section of the text and locate the sections where it is used most frequently. We found 261 occurences of the term, and the whole work is¸about 27,000 lines long. So circa one in hundred lines has the term. Looking at the text, a typical paragraph seems to be around 15 lines. On a printed book, a page is somewhere around 20 to 40 lines of text. 

We can try different sizes for our section of text, but going for a window of around 5 pages or 10 paragraphs might make sense as a starting point. This translates roughly to 150 lines. Like previously, fix the code in [dostoyevsky3.py](./dostoyevsky3.py) and run it.

The output should again be readable as a .csv -file, and thus can be opened in Excel, OpenOffice, Google Sheet, etc. for visualization purposes. Try making a chart out of that, and see how varying the window size affects the results.
