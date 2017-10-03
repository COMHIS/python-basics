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

### Exercise Program flow 1:

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


### Exercise Program flow 2:
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
The output has 


### Exercise Program flow 3:




## Control





