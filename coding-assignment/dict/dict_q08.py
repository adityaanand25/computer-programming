#you have two dictionaries with overlapping keys. Write a program to combine them such that values from the second dictionary overwrite those from the first.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_dict = {**dict1, **dict2}
print(combined_dict)
