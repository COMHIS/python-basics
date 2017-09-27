# Suddenly in Dostoyevsky

Researchers in Russian literature have been discussing the surprisingly high frequency of the word _vdrug_ (translating roughly to _suddenly_) in Dostoyevsky's novels. They've been arguing that the unexpected has a central role in Dostoyevsky's works, and many have been counting the uses of the word _vdrug_, to be able to focus on the nature of that element. We'll do a similar excercise here. 

There are structures utilized her that we have not covered yet, and you don't need to worry about those. Your task is to modify the code so that it will produce the expected results. The lines you need to modify are preceded by comments starting with `# MODIFY HERE`.

---

## Counting "suddenly"

We'll expand the script in a few steps. First, let's read the text from a file, and count the lines with the word `suddenly` in them. Save the script files (right click & save as) <a href="https://raw.githubusercontent.com/COMHIS/python-basics/master/2_basic_concepts/intros.py" download>intros.py</a> and [dostoyevsky1.py](https://raw.githubusercontent.com/COMHIS/python-basics/master/2_basic_concepts/dostoyevsky1.py) into a directory on your computer, and modify `dostoyevsky1.py` so that it will run without errors. You will also need to load the source text file [the_idiot.txt](https://raw.githubusercontent.com/COMHIS/python-basics/master/2_basic_concepts/the_idiot.txt) and save it in that save directory.

You should end up with the text `Total 261 lines with the term "suddenly" found.` printing in terminal.

**Note:** We will use the term _index_ in the code comments. That is yet another basic concept in programming, and generally refers to the order in which items appear in a list. For example, think of a name as a list letters: The name _Ivan_ has 4 letters, in order of appearance: I, v, a, n. Now let's think of that as a list of letters. Also, in programming an index usually starts with 0. So, the indices of the letters in the name _Ivan_ would be: I:0, v:1, a:2, n:3. So, of we wanted to get the letter matching the index 2 in _Ivan_, we would end up with 'a'. Same goes for any list, be it numbers, letters or lines of text, as in our case here.

## "Suddenly" concordance

We want to know in more detail what is happening around "suddenly" in the text. For this we'll employ a linguistic concept called _concordance_, which is explained [here](https://www.nottingham.ac.uk/alzsh3/acvocab/concordances.htm).

Now we also want to save our output, and produce a similar concordance output as in the example in the link. After modifying [dostoyevsky2.py](./dostoyevsky2.py) correctly, you should have a results file with that.

**Bonus assignment:** For those who want to do one. We seem to have produced valid .tsv format there. Find a way to open the output file we produced in a spreadsheet program.

## "Suddenly" over the whole work

Let's have a more statistical overview of the use of "suddenly" in _the Idiot_ now. We'll want to create a measure to track the "suddenliness" of a limited section of the text and locate the sections where it is used most frequently. We found 261 occurences of the term, and the whole work is¸about 27,000 lines long. So circa one in hundred lines has the term. Looking at the text, a typical paragraph seems to be around 15 lines. On a printed book, a page is somewhere around 20 to 40 lines of text. 

We can try different sizes for our section of text, but going for a window of around 5 pages or 10 paragraphs might make sense as a starting point. This translates roughly to 150 lines. Like previously, fix the code in [dostoyevsky3.py](./dostoyevsky3.py) and run it. 

**Bonus assignment:** The output should again be readable as a .csv -file, and thus can be opened in Excel, OpenOffice, Google Sheet, etc. for visualization purposes. Try making a chart out of that, and see how varying the window size affects the results.

**Note:** A window here means gradually moving over the whole text, and focusing on a limited number of lines at a time. So, as a start, we'll consider the first 150 lines of the text, and count the lines satisfying our criteria there. Then we move the window by one line: Now we consider lines 2-151, and count total hits for that subsection of the text. We'll keep on moving the window- lines: 3 to 152, 4 to 153, 5-154, ... 205-354, ... etc, until we reach the end of the text. Thus we have scanned the whole text, and have total number of hits for each subsection of it. [Here's another explanation of that concept](http://www.business-science.io/timeseries-analysis/2017/07/23/tidy-timeseries-analysis-pt-2.html#rolling-window-calculations).
