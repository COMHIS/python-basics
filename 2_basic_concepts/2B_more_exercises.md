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

There are two major exceptions to the normal top down order of processing, namely _loops_ and _functions_. Loops are same
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

Another major exception to the processing order are functions. Functions are actually bits code, that are written 
somewhere else but read here! We'll get to functions in more detail later on.

## Control




