Question: Reverse the order of words in a string.

def reverse_words_order(input_string):
    words = input_string.split()
    return " ".join(reversed(words))
