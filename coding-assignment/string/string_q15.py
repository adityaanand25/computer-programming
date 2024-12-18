Question: Find the first non-repeated character in a string.

from collections import Counter
def first_non_repeated_char(input_string):
    char_count = Counter(input_string)
    for char in input_string:
        if char_count[char] == 1:
            return char
    return None
