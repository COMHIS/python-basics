## Iterations II

Now we can look again the iteration thing, knowing little bit more about the things (list-like-things) we are iterating.

**Iterating lists**

Lists can be iterated in two different ways:
1) running through all the items in a list
2) running through list of numbers as long as the list and using those numbers to access elements with corresponding indices in the list

```python

my_string = "Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice."
my_list = my_string.split(" ")

#method 1: Iterate item by item

for x in my_list:
    if len(x) > 3:
        print(x)
        
Many
years
later
faced
...

#method 2: Iterate indices

for i in range(0,len(my_list)):  #NOTE function range(a,b) returns numbers from a to b-1
    if len(my_list[i]) > 3:
        print(x)
        

Many
years
later
faced
...

```

The main difference between these two is that a list can not be changed while it is being iterated, so we can not remove or add new items to a list with method 1, nor can we change the values in the list.

This restriction is circumvented with method 2, as we are not iterating the list itself, nearly a list of numbers with equal length.

Other reason to use the method 2 would be that it provides a handy way of accessing adjacent items:

```python

for i in range(0, len(my_list)):
    if my_list[i] == "Colonel":
        print(my_list[i-1], my_list[i], my_list[i+1])

squad,   Colonel   Aureliano

```

### Iterating dictionaries

Like said above, items stored in dictionaries are key-value pairs and the values are accessed by their keys (but not the other way round). And also was mentioned before was that keys are not stored in dictionaries in any specific order. This means that if you iterate the same dictionary many times over during your code, the order might be everytime different, or then it might not.

In practice dictionaries are iterated like this:

```python
my_dict = {"has":34, "is": 59, "a":12}

for key in my_dict:
    print(key)
    if my_dict[key] > 50:
        print("over fifty!")
        
a
is
over fifty!
has
```

---