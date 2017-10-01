# Suddenly in Dostoyevsky continued

We'll do a short dive back to Dostoyevsky, and explore how can we develop our concordance -measure further.

---

## Concordance revisited

Let's start with the concordance code from last time, and apply that to another source text, "The Brothers Karamazov". Do as you did previously, and save [intros.py](https://raw.githubusercontent.com/COMHIS/python-basics/master/3_basic_concepts_ii/intros.py) and [dostoyevsky_concordance.py](https://raw.githubusercontent.com/COMHIS/python-basics/master/3_basic_concepts_ii/dostoyevsky_concordance.py) into a new directory.

Have a look at dostoyevsky_concordance.py with your text editor and see if you can figure out how it works. Pretend you are the Python interpreter, and go through it line by line, and figure out what the computer does on each line. After you've understood the logic of the script, run it. It should work out of the box and create a file with the results.

## suddenly 2-grams

Next, we'll modify our code a bit. Instead of printing out the lines containing 'suddenly', we'll find the preceding and following words, count the occurences for each word and save the results in a table.
