Question: Find the longest word in a string.

def longest_word(input_string):
    words = input_string.split()
    return max(words, key=len)
