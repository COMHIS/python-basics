# Part 2 - Basic concepts in programming

This part will introduce the basic rationale behind a program and introduce some of its key components. Next, we'll try those concepts in practice with small coding excercises. After that we will dive into a basic example where these are applied in quantitative literary study.

**Note:** We'll occasionally use the term _script_ here. That term refers to the program code that we're writing.

If the following is trivial for you, skip straight into the [Dostoyevsky -text analysis part](./suddenly.md). 

---

## Concepts to be covered

### Input and output

A program's function is to process data, in one form or other. It takes in data provided by the user (input) and produces a result based on that (output). An example of this would be:
**input:** Text of the _Crime and Punishment_ by Dostoyevsky.
**output:** An analysis of word use in that text.

You can think of a script as a machine that processes raw material into usable form. Throw in a lump of metal and out comes a screw to be used. Insert a pile of library catalogues, and receive a quantitative representation of book history.

### Program Flow

At the very basic level a program script is processed one line at a time, starting from top and ending at the bottom.

There are various means to control that flow to skip or repeat parts of the script. Of those we'll cover the most fundamental ones, called _conditional statements_, also know as _if-then-else_ -statements.

### Variables and values

While a program is running it needs to keep the data somewhere. Those locations where the data is kept are called _variables_. Those variables have names and the data those variables hold are called _values_.

* A **string** variable holds text. For example: "Hello World!"
* An **integer** variable holds integers (numbers with no decimal point). For example: 100 or 23 or 5
* A variable called **float** holds numbers that can also have decimals. For example: 62.78 

----

## Small exercises

For each of these, create a script-file, like you did previously with the _Hello World!_ -task, and run that script with Python, as you did previously. We'll walk thourgh the process once again in the first example.

**Note:** Code can become messy fast. There are various ways to combat that, and one of those is called commenting. In the following excercises you'll notice explanatory text on rows preceded by the character '#'. That's the way commenting is done in Python. Everything on the row after that character is ignored by the Python-interpreter.

### Variables and values 1

Open your text editor, and write in the following code:

```python
course = "Introduction to Digital Humanities"
```
We just created a variable. It's name is 'course', and it holds some text. Let's print that variable now, just like we previously did print the text "Hello World!". Add the following on a row below the above one:
```python
print(course)
```
The script in your editor should now look like this:
```python
course = "Introduction to Digital Humanities"
print(course)
```
Save it with a name of your choosing (`task1.py` for example), and run it in terminal with the command:
`python3 task1.py`
If you forgot how to use the terminal, refer back to the materials for part 1.

**Note:** Another term for running a script is "execute". We'll probably use that in the instructions too, just to break the monotony.

### Variables and values 2

Lets try modifying a variable now, and doing some basic primary school mathematics. Create a new script, or change the previous one, and save execute it when appropriate.

We're dividing apples among kids again. Hooray.

Type the following in your script, save and run:
```python
old_apples = 12
new_apples = 13
# So, there are 12 old and 13 new apples. Let's figure out how many in total.
# So add the numbers up, and store the results in another variable:
total_apples = old_apples + new_apples
# ... and let's print the results.
print(total_apples)
```
You should see the number `25` print out.

### Variables and values 3

Now, do some coding of your own. Fill in the blanks to this incomplete script to figure out how many apples per kid there are, and make sure it runs without errors:
```python
apples = 12
kids = 3
# note: division is done by the / -operator. Complete the below line:
apples_per_kid =
# ... and let's print the results again:
print("Apples per kid:")
print(apples_per_kid)
```
The completed script should print out the text `Each kid can have 4.0 apples.`. Note that we did some manipulation with the _string_ variables too, inside the print command.

### Variables and values 4

One last one with variables and values, by your own this time. Imagine there are:
* 4 kids
* 3 apple trees
* 21 apples per tree
* a harsh apple tax of 9 apples.

Write a code that figures out how many apples are left per kid after the following steps:
* Each tree is picked bare, and the apples are placed together in ine big basket.
* The apple tax is reduced from the basket.
* The apples are divided among the kids.

Place the various values in appropriately named variables, do the required maths operations, and print the results. Look at the previous bits of code for clues on how to proceed. You should end up with printing a phrase like this: `Each kid gets 13.5 apples.`

A programming task is solved like that breakdown above. Break a big task (not very big here) into small components, solve one component at a time, and end up with the results.

### Flow and flow control 1

Another very common variable type is called _boolean_. That one holds a value which is either _True_ or _False_. Among other things, booleans are used in program flow control. Booleans are assigned values like this:
```python
are_we_finished = False
is_this_easy = True
```

Another concept utilized in flow control is evaluation: We'll check the boolean value of a statement, for example if one value is greater than another. Comparison operations include:
* `x > y` Is x greater than y? If yes, the result is `True`, otherwise the result is `False`
* `x < y` Reverse above.
* `x == y` Is x equal to y? If yes, the result is `True`, otherwise the result is `False`
* `x != y` Are x and y different values?

Try running the following code. You should see `False` print out.
```python
# We'll set a few variables:
cats = 5
dogs = 7
# And now we'll compare those:
# Are there more cats than dogs in our variables?
more_cats = cats > dogs
# Booleans don't need to be explicitly converted to strings for printing ...
print(more_cats)
```

### Flow and flow control 2

Let's do something with those comparisons now. Get aquinted with the _if-else_ -elements:

```python
my_name = "Joe"
if my_name == "Ann":
    print("Welcome " + my_name)
else:
    print("Greetings " + my_name)
```
Depending on the value of the my_name -variable the script prints different greetings. Ann gets a special greeting, others don't. The part after `if` needs to evaluate to either `True`or `False`. If it evaluates to `True` it is executed, and if not, it is skipped. In case the if -block is followed by `else`, and the if -part was not executed, the part in else is executed instead.

**Note:** Indentation. The code "inside" the if- and else-statements is indented by four spaces. Indentation is the way Python knows what parts of code are covered by the conditional statement.

### Flow and flow control 3

Try the if-else blocks yourself now. Write a script that assigns a number to a variable, and then evalyates that. Try different operators, and print a message if the evalution is true. Here's a few examples to get you started:

```python
frustrated_attempts = 6
if frustrated_attempts > 4:
    print("This is starting to get frustrating!")
else:
    print("Doing fine still.")
```

```python
# Actually you don't need the else statement always. Depends on what you want to do:
cats = 5
if cats < 10:
    print("not enough cats")

if cats == 5:
    print("There seems to be exactly 5 cats")

if cats != 5:
    print("Definitely not 5 cats.")

```

## Suddenly in Dostoyevsky

We've done enough small exercises now. Let's have a look at a small concrete data science example now. Follow on to an [assignment on analysis of Dostoyevsky's Idiot](./suddenly.md).
