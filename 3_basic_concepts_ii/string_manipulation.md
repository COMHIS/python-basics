
## String manipulation

The matter of fact is that strings in Python are little more than lists of characters. Almost all operations that can be done on lists, can be done on strings as well. So certain characters in a string can be accessed by its position, string can be sliced by indices. Also lists and strings utilize the '+' sign in similar way:

```python
my_string_A = "Hopefully this"
my_string_B = "is helpful"

my_list_A = ["Hopefully", "this"]
my_list_B = ["is", "helpful"]

print(my_string_A + my_string_B)
"Hopefully thisis helpful"
print(my_list_A + my_list_B)
["Hopefully", "this", "is", "helpful"]
```

A string manipulation function that you will see used frequently is `.split()`. It, as the name implies, splits strings into lists of smaller strings, and with the default argument does that at all [_whitespace_](https://en.wikipedia.org/wiki/Whitespace_character) (that is, spaces, end of lines, tabs, etc.) characters.

---

## Exercises

### String manipulation 1

Strings are sliced just like lists. Try getting the first 5 characters (remember, slicing was done by `name_of_list[start:end]`) from the following string, and print those:

```python
some_string = "Strings are sliced just like lists. Try getting the first 5 characters from the following string."
```

### String manipulation 2

Let's try splitting that above string into words now. Split the string using the `.split()` -function, save the results in another variable, and print the fourth word in the resulting list. You should see `just` print out.
