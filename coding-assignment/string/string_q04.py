Question: Find the most frequent character in a string.

def most_frequent_char(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return max(char_count, key=char_count.get)
