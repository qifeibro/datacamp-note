"""
using Python's built-in function enumerate().
This function is useful for obtaining an indexed list
suppose you had a list of people that arrived at a party you are hosting.
The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.)
"""

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

indexed_names = []
for i in range(len(names)):
    index_name = (i, names[i])
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, start=1)]
print(indexed_names_unpack)
