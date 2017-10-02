
### String manipulation

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

---
