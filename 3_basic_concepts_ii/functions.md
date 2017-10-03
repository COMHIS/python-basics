## Functions

We have been using _functions_ a lot already. Almost every command we've employed so far, from `print()` to `len()` and `quit()` are functions. A function is basically a simple independent program with its own input and output. A function's input are the paramenters that are given to it inside the parenthesis following its name. For example:

```python
print("Some text!")  
```

The `print()` -function above was given a string with the text "Some text!" as an input. The output of that is printing that text in terminal. Another example would be:

```python
string_length = len("Another string of text.")
print(string_length)
```

The function `len()` is given a string as a parameter. That function counts
length of various objects, in this case that string. The output of the function (23) is then stored in the variable `string_length`. That variable is in turn given to the familiar funtion `print()` as an input, and printed out, like we would expect print to do.

---

### Defining your own

As mentioned before, the benefit of writing a program to do some task is that we can automate a repeating task. That holds for parts of those programs too. Say, of we wanted to take the previous birthyear- example and test for the adulthood/minority for a variety of years in time, we would end up writing the same code multiple times. A solution is to write a function of our own: We want to create a single command that is given a birthyear and a historic year as parameters, and that tells us if that person was an adult or not on that specific year. So, let's do that:

```python
def is_adult(birthyear, historic_year):
    if historic_year - birthyear > 17:
        return True
    else:
        return False 
```

So, what happens in the above code? We start with a line that tells Python that we are defining a function. That's the `def` -command there. Then we give the name of the function that we are creatign `is_adult`, and the parameters that it accepts: `(birthyear, historic_year)`. We finish with `:` to tell Python that we are starting a code block whit the actual things that the function does.

Within the function we compare the two variables that are given to it as parameters, and with the `return()` command tell what the output will be. So, if the age of the person on the given year is greater than 17, our function returns the value `True`, and otherwise it returns the value `False`.

We would use our function in our script like this:

```python
def is_adult(birthyear, historic_year):
    if historic_year - birthyear > 17:
        return True
    else:
        return False 


birthyear_aino = 1922
birthyear_maija = 1933
year = 1945

# The following places True in is_adult_aino 
# functions are given the parameters in the same order as
# they were in the definion.
is_adult_aino = is_adult(birthyear_aino, year)
# let's print that too ...
print(is_adult_aino)

# And this one is False ...
# alternatively you can give parameters by specifying their names
# when calling the function. In that case, the order does not matter
is_adult_maija = is_adult(historic_year=year, bithyear=birthyear_maija)
print(is_adult_maija)
```
---

## Exercises

**Note:** As before, each exercise is independent unless otherwise stated, so start each one in a separate script file, or erase old code from the one you use for doing them. Don't paste them all one after the other!

---

### Functions 1

Let's try creating a few functions now. Something really simple as a warm up:

```python
def multiplier(number_a, number_b):
   result = number_a * number_b
   return result
```

We created a function that takes two numbers, and returns the result of multiplying them. Let's use that function now, and print the results to see what happened:

```python
def multiplier(number_a, number_b):
   result = number_a * number_b
   return result

a = 2
b = 6
result_of_multiplication = multiplier(a, b)
print(result_of_multiplication)
```

Create a similar function now, but for adding two numbers together. Use it and print the results out. 

### Functions 2

Let's go back to our adult/minor exercise, and pack some of the code there into a function. Previously, printing the age group was done like this:

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]

for birth_year in birth_years:
    age = 1944 - birth_year
    if age > 17:
        print("Adult")
    else:
        print("Minor")

```

We'll modify that a bit now and instead create a function that we will call inside the loop. Note that this function doesn't really return anything. It just prints the result:

```python
def print_agegroup(birth_year, historic_year):
    age = historic_year - birth_year
    if age > 17:
        print("Adult")
    else:
        print("Minor")


birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]
historic_year = 1942

for birth_year in birth_years:
    print_agegroup(birth_year, historic_year)
```

Now, modify the function that instead of printing the text "Adult" or "Minor" it will return it as a string. Place that in a variable within the loop and print that variable.

### Functions 3

We've been adding strings together quite a few times previously. As you remember, that went like this: `combined_string = "Digital Humanities" + " is " + "great!".` Let's do that in a function now.

```python
# We'll define a function that takes a string, and returns
# that same string with " the cat" added 
def get_cat_name(name):
    cat_name = name + " the cat"
    return cat_name

# and to use that function:
name1 = "Catty"
name1_catted = get_cat_name(name1)
# and print the catname:
print(name1_catted)

# we can do that inside the print -function too:
print(get_cat_name("Meow"))

# and we can also loop that over a list:
names = ["Joe", "Milly", "Andrei", "Anja-Riitta", "Musti", "Sigge"]
for name in names:
    print(get_cat_name(name))
```

Do something similar yourself. create a function that makes names into houseplant names, like this- from "Joe" to "Green Joe the houseplant". Create the function, and try it out over a list.
