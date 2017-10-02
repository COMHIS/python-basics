## Indentation / Blocks of code

With the conditional statements (if & else) and iterations (for -loops) we encountered indented code. An example from last part would looked like this:

```python
ages = []
for member in member_registry:
    birth_date = member["birth_date"]
    age = date(1944, 9, 19) - date(birth_date)
    ages.append(age)
```

Everything indented together on the same level of indentation constitutes a _code block_, that is to say, a series of commands grouped together. The block starts with a line ending with colon `:`, which is typically a conditional statement, loop or a function definition (more on those next). The block ends when there's a line that is not indented. Like this:   

```python
ages = []
for member in member_registry:
    birth_date = member["birth_date"]
    age = date(1944, 9, 19) - date(birth_date)
    ages.append(age)
print(ages)
```

Lines from `birth_date ...` to `ages.append(age)`are part of the code block insode the for -loop. The final `print(ages)` -command is not part of the block.

A code block can be inside another code block, like we saw in the last examples of the previous part:

```python
birth_years = [1928, 1924, 1921, 1928, 1926, 1921, 1922, 1926, 1927, 1929]

for birth_year in birth_years:
    age = 1944 - birth_year
    if age > 17:
        print("Adult")
    else:
        print("Minor")
```

Above, the code block holding the contents of the for-loop also has two smaller 1-line blocks inside it: the `print("Adult")` and the `print("Minor")` blocks are contained within the block for the loop.

Think of _code blocks_ as small semi-independent sections of code that have their own small task to perform.  
