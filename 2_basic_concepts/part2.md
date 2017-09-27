# Part 2 - Basic concepts in programming

This part will introduce the basic rationale behind a program and introduce some of its key components. Next, we'll try those concepts in practice with small coding exercises. After that we will dive into a basic example where these are applied in quantitative literary study.

There's first a short theory part, and then some exercises. Don't worry if you don't get the "theory" on the first reading. Just go on into the exercises, and refer back to the first section. It will start to make more and more sense, eventually.

**Note:** We'll occasionally use the term _script_ here. That term refers to the program code that we're writing.

**Note:** At some point you'll want to use a bit more sophisticated editor than Notepad, TextEdit, etc. [See here for alternatives.](./editors.md) That point might as well be now.

If the following is trivial for you, skip straight into the [Dostoyevsky -text analysis part](./suddenly.md). 

---

## Concepts to be covered

### Input and output

A program's function is to process data, in one form or other. It takes in data provided by the user (input) and produces a result based on that (output). A program may be as simple as:

**input:** Firstname Lastname

**output:** firstname.lastname@helsinki.fi

Programs may be written to complete simple intermediary tasks in a longer work flow, such as:

**input:** Excel sheet

**output:** The same Excel sheet, but rows filtered by some condition, and one of the columns split into two columns.

A more DH example of this would be:

**input:** Text of the _Crime and Punishment_ by Dostoyevsky.

**output:** An analysis of word use in that text.

You can think of a script as a machine that processes raw material into a different form. Whether it takes digital plywood planks and orders them by length and adds a tiny hole in the middle, or smashes them all into splinters, looks for those with grayish hue and counts them.

---

### Program Flow

Like stated before, a program consists of operations executed on some input. Program is in that sense not quite unlike a mathematical function:

_f(x) = y_

where x is input and y output. In fact, many operations in the program are written as _functions_. A program can consist of a single function, a huge labyrinth of nested functions, where inputs and outputs criss-cross until the final output is returned, or as most often, something in between.

At the very basic level a program script is processed one line at a time, starting from top and ending at the bottom. Each row contains some kind of command that takes the program one step further.

There are various means to control that flow to skip or repeat parts of the script. Of those we'll cover the most fundamental ones, called _conditional statements_, also know as _if-then-else_ -statements.

An if-else statement looks like this in python:

```python
age = 16
if age > 17:
    print("This person is an adult in the legal sense.")
else:
    print("This person is still a minor.")
```

In case the condition specified after `if` is true, the indented lines are run normally. If the condition is not true, the portion after `else` is run instead. In our example the _variable_ age (of some person we are considering in the code, presumably) does not satisfy our condition, and therefore we'll print out the line stating that the person is a minor. What is a _variable_ then? Follow on to the next section:

---

### Variables and values

While a program is running it needs to keep the data somewhere. Those locations where the data is kept are called _variables_. Those variables have names and the data those variables hold are called _values_.

* A **string** variable holds text. For example: "Hello World!"
* An **integer** variable holds integers (numbers with no decimal point). For example: 100 or 23 or 5
* A variable called **float** holds numbers that can also have decimals. For example: 62.78 

You can think of variables as kind of shorthand ways of referring to things, or identities you give to pieces of text or numbers so you call them the same name even if their values would change.

Imagine a circumstance where you are interested in [Lotta Svärd organisation](https://en.wikipedia.org/wiki/Lotta_Sv%C3%A4rd) and want to know mean age of its members when the Continuation War ended. To begin with, you only have the organisation's member registry that contain members' birth dates but no age. What your program would do, would be to calculate the difference between each member's birth date and 19.9.1944, store them, and calculate the mean.

You would write your program to do something like this:

* take _birth_date_ as **input**:
* calculate _age_ = "19.9.1944" - _birth_date_
* **output**: _age_

And repeat this for each member in the registry. While each member is treated in turn, we assign the name _birth_date_ to refer to the birth date of that respective member. Running exactly the same operation to long list of items is what makes programming a very powerful tool. This takes us to the next step, called:

---

### Iteration

Iteration means that we repeat the same process identically a number of times. Iteration (some times called as _loops_) can take many forms, here we present the most usual way this is done in python, called **for**-loops.

The idea of a **for** loop is that it takes, as an input, something that can be iterated (usually a list of some kind), and goes through each member of that iterable thing in turn until it reaches the end. And that's it.

So let's write the example above in to a python code:

```python
ages = []
for member in member_registry:
    birth_date = member["birth_date"]
    age = date(1944, 9, 19) - date(birth_date)
    ages.append(age)
```

This is now little bit complicated looking, but it actually would do the job. Let's walk through the code one row at a time.
* The part "ages=[]" builds a new, empty list into the computer's memory. In order for us to store the ages, we need something to store them into. This is how we do that.
* for member in member_registry is the iteration operation. We tell the computer to go through the _member_registry_ database on row at a time, and on each iteration, call that row _member_.
* The member_registry is a database, so it is form of key-value pairs, which means that different kinds of information is stored under different headings. We assume that our imaginative Lotta Svärd member registry contains not only birth dates, but other information as well, say birth place, education, rank or office at the organisation etc. On the row birth_date = member["birth_date"] we specify that we are interested on the birth date data of each member.
* On the row age = date(1944,9,19) - date(birth_date) the real magic happens. We have imported a library called _datetime_ that contains a number of ready-made calendar related functions. By giving a date to its _date_-function, we turn it into a thing we can simply run calculations on. Such as subtraction here.
* In the final row of the loop, we take the output of the previous row (_age_) and add it to the list we created on the first row.
* When the loop has run its course to the end, we have list of all the ages of all the members in the member_registry on a specific date (19.9.1944).

----

## Small exercises

For each of these, create a script-file, like you did previously with the _Hello World!_ -task, and run that script with Python, as you did previously. We'll walk through the process once again in the first example.

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
Remember to add a blank line at the end. As mentioned previously, all python scripts end with a blank line.

Save it with a name of your choosing (`task1.py` for example), and run it in terminal with the command:
`python3 task1.py`
If you forgot how to use the terminal, refer back to the materials for part 1.

**Note:** Another term for running a script is "execute". We'll probably use that in the instructions too, just to break the monotony.

### Variables and values 2

Lets try modifying a variable now, and doing some basic primary school mathematics. Create a new script, or change the previous one, and save and execute it when appropriate.

First we manipulate a string variable:

```python
course = "Introduction to Digital Humanities"
print(course)

evaluation = "is teh best"
print(course + " " + evaluation)
```

Next we'll move to integers. We're dividing apples among kids again. Hooray.

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
print("Apples per kid: " + str(apples_per_kid))
```

**Note:** There is a `str()` -command inside the print function. This is called _casting_. What happened there was converting a value in one variable type to another, namely making a _string_, that is, text, out of a _float_, a number. This was necessary so that we could combine it with the other _string_ -type variable, the text "Apples per kid: ".

The completed script should print out the text `Apples per kid: 4.0`. Note that we did some manipulation with the _string_ variables too, inside the print command.

### Variables and values 4

One last one with variables and values, by your own this time. Imagine there are:
* 4 kids
* 3 apple trees
* 21 apples per tree
* a harsh apple tax of 9 apples.

Write a code that figures out how many apples are left per kid after the following steps:
* Each tree is picked bare, and the apples are placed together in one big basket.
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
are_there_more_cats = cats > dogs
# And print that out:
print(are_there_more_cats)
```

### Flow and flow control 2

Let's do something with those comparisons now. Get acquainted with the _if-else_ -elements:

```python
my_name = "Joe"
if my_name == "Ann":
    print("Welcome " + my_name)
else:
    print("Greetings " + my_name)
```
Depending on the value of the my_name -variable the script prints different greetings. Ann gets a special greeting, others don't. The part after `if` needs to evaluate to either `True`or `False`. If it evaluates to `True` it is executed, and if not, it is skipped. In case the if -block is followed by `else`, and the if -part was not executed, the part in else is executed instead.

**Note:** Indentation. The code "inside" the if- and else-statements is indented by four spaces. Indentation is the way Python knows what parts of code are covered by the conditional statement. More generally, the indented sections are used to separate smaller semi-independent sections of code, and they will be covered more in detail next time, when we learn more about _functions_.

### Flow and flow control 3

Try the if-else blocks yourself now. Write a script that assigns a number to a variable, and then evaluates that. Try different operators, and print a message if the evaluation is true. Here's a few examples to get you started:

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
    print("There seems to be exactly 5 cats here!")

if cats != 5:
    print("Definitely not 5 cats.")

```

### Iteration 1

Let's imagine a small subset of that Lotta Svärd -database mentioned earlier. We'll find out the ages of a group of people there, find the mean (average) of those and the oldest and youngest person in that group.

For the sake of the exercise we'll make up some imaginary data. We'll also make it a bit easier and forget about real dates now, and just use a list of years.

A _list_ in python is declared like this:

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]
```

In the above code we declared a 10-item long list of numbers (integers). Add a few more yourself, and try to print it. 

Let's figure out the ages in 1944 for those birth years next. We'll employ the _for_-loop that we learned about. To know the age for each birth year (this is not how you figure out sobodys age in reality, but close enough for now), we should subtract that year from the current year. We'll print out the ages as we figure them out, just to see what's happening.

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]

for birth_year in birth_years:
    age =  1944 - birth_year
    print(age)

```
**Note:** In our for -loop statement we created a variable `birth_year` that exists only inside that loop. A structure like that is extremely common when iterating over a list.

Next, let's figure out the average age. To find the average, we'll create a _variable_ where we will sum all the values in the list and then divide it by the length of the list. There's a handy function `len()` that will get us the length (number of values stored in) of a list.

During each iteration of the list, we'll add the age for that birth year to our running total. Notice how during each iteration we reassign a new value to the variable where we hold the total, like this: `age_total = ages_total + age` To break that down: We'll take the value previously stored in `ages_total`, add `age` (which we figure out anew during each iteration) to that and place this new value in `ages_total`. After iterating through all of the `birth_years` we'll divide the sum by their amount and print the results.

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]

number_of_birth_years = len(birth_years)

ages_total = 0
for birth_year in birth_years:
    age = 1944 - birth_year
    ages_total = ages_total + age

average_age = ages_total / number_of_birth_years
print("Average age: " + str(average_age))

```

### Iteration 2

We can easily have an if-else -statement inside a for-loop. Let's iterate through all the ages in our imaginary data of birth years and print out different texts, depending on the age we end up with. Try running the following:

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]

for birth_year in birth_years:
    age = 1944 - birth_year
    if age > 17:
        print("Adult")
    else:
        print("Minor")

```

Now, based on the previous two examples, make a script that finds the total number of adults and minors in our sample data, and prints out the results. The steps for that are:

1. Copy the above code to act as a base that you will modify.
2. After the line with the birth_years -list, create two variables (set to the value 0) to track the number of adults and minors.
  * For example, the variable tracking the amount of minors could look like this: `minors = 0`.
3. Instead of printing either "Adult" or "Minor" inside the loop, increase the corresponding variables by one.
  * Using the above minors-variable as an example: instead of `print("Minor")`, the line would read: `minors = minors + 1`.
4. After the loop is finished print out the values in the variables holding the numbers for minors and adults.
  * Remember to pay attention to the indentation! The print -commands should not be inside the loop, so they should have no indentation.

### Iteration 3

One last exercise! Lets find the youngest and oldest age in our imaginary dataset. Like previously, we'll iterate over the whole list. We'll have a variable that keeps track of the youngest age encountered, and changes it if the iteration encounters a smaller number:

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]

# we'll put something really high here at start... 
lowest_age = 1000
for birth_year in birth_years:
    age = 1944 - birth_year
    if age < lowest_age:
        lowest_age = age

print("Lowest age was: " + str(lowest_age))

```

Copy the code, modify it to find out the highest age in the dataset, and print that out.

## Suddenly in Dostoyevsky (input & output)

We've done enough small exercises now. Let's have a look at a small concrete data science example now. Follow on to an [assignment on analysis of Dostoyevsky's "the Idiot"](./suddenly.md) to explore the practical uses of coding in digital humanities and to get an example of research related input->script->output -process.
