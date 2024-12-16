# Remove Duplicate from List
"""
The .fromkeys() method returns a dictionary with a specified set of keys.
It can also initialize the entries with a specified value.

dict.fromkeys(iterable, value) - 
if empty iterable is passed, it will return an empty dictionary.
"""


def remove_duplicate(myList):
    newList = list(dict.fromkeys(myList))
    return newList


myList = [1, 2, 2, 3, 4, 4, 5]
stringList = ["a", "b", "b", "c", "d", "d", "e"]
print(remove_duplicate(myList))
print(remove_duplicate(stringList))
