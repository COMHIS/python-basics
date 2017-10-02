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

#### Defining your own functions

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