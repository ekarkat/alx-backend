my_dict = {'a': 1, 'b': 2, 'c': 3}

# Get an iterator over the dictionary's items
iterator = iter(my_dict.items())

# Use next() to get the first item
first_item = next(iterator)

print("First item in the dictionary:", first_item)
print(type(first_item[0]))