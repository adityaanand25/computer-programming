Question: Check if all characters in the string are unique.

def has_unique_characters(input_string):
    return len(set(input_string)) == len(input_string)
