# Complementary exercises for part 2

## Program Flow

Program flow means simply the way the computer reads the commands coded in the script. In most cases the program is read 
one line after another top down. Only things defined or named earlier in the code are available for commands below them.

Executing the script:
```python
string = "Amsterdam, Netherlands"
print(string)
```
will result in the text
Amsterdam, Netherlands
being shown in the terminal.

However, script:
```python
print(string)
string = "Amsterdam, Netherlands"
```
will result in text 
'NameError: name 'string' is not defined'.
This is an error message which tries to inform us that we are asking the computer to do something (in this case print) 
to some object that its never heard of so doesn't know what to do. This is one of the most common error messages and we
will return another case it might result in later on.

There are three major exceptions to the normal top down order of processing, namely _loops_ and _functions_. Loops are same
thing we have discussed earlier as iteration: the program is commanded to repeat a certain segment of code until some
defined requirement is met, after which it proceeds normally:

```python
print("starting here")

for i in range(0,5):
    print("repeating")
    
print("end here")
```
This will produce output like this:

starting here
repeating
repeating
repeating
repeating
repeating
end here

The program repeats the command print("repeat") and add 1 to the value of the variable _i_ until reaches value 5 and then 
continues forward. The function range(0,5) defines the sequence of values _i_ is given every round, so in this case values
0, 1, 2, 3, 4.

Second major exception to the processing order are functions. Functions are actually bits code, that are written 
somewhere else but read here! We'll get to functions in more detail later on.

The third exception are conditional clauses. In this case the program only proceeds to the block defined below if some condition is met. These are like natural language if-clauses: the program stops to ask a specific if-question and proceeds according to the answer.

The syntax for _if_-clause in Python is as follows:

if condition:
    run this indented block
else:
    run this indented block instead
    
The condition part can be written in many ways. Probably the most common one is 

### Exercise Program flow 1: normal flow

Copy paste the following script in your text editor and save it as 2B_flow1.py.

```python
text = "LONDON. Michaelmas Term lately over, and the Lord Chancellor sitting in Lincoln’s Inn Hall. Implacable November weather."

text = text.lower() #turns all characters to lower case

text = text.replace("n", "") #removes all letters n 

text = text.replace("a", "aA") #adds A after each a

print(text)
```
Re-order the commands so that the output in the terminal is:
A) london. michaaelmaas term laately over, aad the lord chaacellor sittig i licol’s i haall. implaacaable november weaather.

B) lodo. michaaelmaas term laately over, aad the lord chaacellor sittig i licol’s i haall. implaacaable ovember weaather.

**Solution**

A) we see that no characters have been deleted, so there has been no _n_ letters in the _text_ when the rule to remove _n_ letters was applied, as all the n-letters are upper case. From this we know that replace() function has to come before lower() function. As the upper A's have been lowercased also the adding A's has to come after lowercasing lower() function.

B) In here the _N_'s have been dropped, so the removing _n_'s has to come after lowercasing. The A's are again lowercase, so lowercasing must precede the addition of A's.


### Exercise Program flow 2: functions
Again, copy paste the following script in your text editor and save it as 2B_flow2.py.

```python
def alphabet_order(A):
    print("ordering by alphabet")
    return "".join(sorted(A))

text = "LONDON. Michaelmas Term lately over, and the Lord Chancellor sitting in Lincoln’s Inn Hall. Implacable November weather."

text = alphabet_order(text) 

text = text.lower()

text = text.replace("i", "I")

print(text)
```
Re-order the commands so that the result comes out like:

A)                 ,...IIIIIIIaaaaaaaaabbcccccdddeeeeeeeeeeeghhhhhlllllllllllllmmmmmnnnnnnnnnnnoooooooprrrrrrsssttttttvvwy’

B) LONDON. Michaelmas Term lately over, and the Lord Chancellor sitting in Lincoln’s Inn Hall. Implacable November weather.

**Solution**
A) The output has uppercase I's leading the other characters, which means that changing i's to I's must precede the alphabetical ordering. Other characters are ordered in one sequence, which means that overall lowercasing must precede alphabetical ordering as well.

B) This is a trick question of course. The print() function can follow directly the first definition of _text_ variable.


### Exercise Program flow 3: conditions

Again, copy paste the following script in your text editor and save it as 2B_flow3.py.

```python

text = "LONDON. Michaelmas Term lately over, and the Lord Chancellor sitting in Lincoln’s Inn Hall. Implacable November weather."

text = text.lower()

if text.islower():
    text = text.replace("LONDON. ", "")
else:
    text = text+" FIN."
    

print(text)
```

Re-order the code so that the end result is:

london. michaelmas term lately over, and the lord chancellor sitting in lincoln’s inn hall. implacable november weather. fin.



---

## Iteration

Remember, iteration means we will go items in some kind of list or sequence, one at a time. We will employ lists and variables here as well.

### Iteration 1

Let's iterate over a list and print the results out.

```python
list_of_animals = ["duck", "dog", "cat", "human"]
for animal in list_of_animals:
    print(animal)

```

Now, create a new script file and create a list like in our previous example. Make it a list of 5 names, for example. Iterate over that list and print each item in turn, just like we did with the list of animals.

### Iteration 2

Next we'll try actually doing something with the values in our loop. Our dummy-data of 18th century publication years has some errors in it, and we'd like to find them. Modify the code inside the for-loop so that all years that are outside the 18th century are printed out.

```python
publication_years = [1750, 1761, 1775, 1776, 1701, 1702, 1706, 1906, 1765, 1752, 1991, 751, 1789, 1777, 1711]
for year in publication_years:
    if year < 2000:
        print(year)
    if year > 2000:
        print(year)
```

You should print out the years 1906, 1991 and 751.

### Iteration 3

Let's imagine we cleaned up that list of years. We'll want to find the latest publication year in our dataset now. For this we'll set up a varibale that will hold that value, and overwrite it each time we find higher value in our list. We start with highest_year set to 0, as any year will be higher than that. Use the line `highest_year = year` to place the value in variable `year` in the variable `highest_year`. Each time we find a higher year, we will overwrite the previous best result kept there.

Finally, add a new line to print the highest_year after the loop is finished.

```python
publication_years = [1750, 1761, 1775, 1776, 1701, 1702, 1706, 1706, 1765, 1752, 1791, 1751, 1789, 1777, 1711]

highest_year = 0

for year in publication_years:
    if year > highest_year:
        # set highest_year to year on the following line!
        RIGHT_HERE

```

### Iteration 4

Something a bit more challenging now. Let's find the year closests to 1755 in our data. We'll use the function `abs()`, which will turn any integer into a positive integer - so -5 becomes 5, -1 becomes 1, 3 as, it already is positive stays 3, etc. 

Again, modify the code so it will work.

```python
publication_years = [1750, 1761, 1775, 1776, 1701, 1702, 1706, 1706, 1765, 1752, 1791, 1751, 1789, 1777, 1711]

closest_year = 0

for year in publication_years:
    # find the difference between 1755 and the year we are iterating:
    difference = abs(1755 - year)
    # then find the previous best result:
    closest_difference_so_far = abs(1755 - closest_year)
    if difference < smallest_difference:
        # assign year to closest_year here
        RIGHTHERE
        
print(closest_year)
```

