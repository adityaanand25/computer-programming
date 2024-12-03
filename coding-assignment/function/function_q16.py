 Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower
print(count_case('The quick Brow Fox'))
