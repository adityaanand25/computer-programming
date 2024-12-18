Question: Find the length of the last word in a string.

def length_of_last_word(input_string):
    words = input_string.split()
    return len(words[-1]) if words else 0
