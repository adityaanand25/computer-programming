Question: Count occurrences of each word in a string.

def count_word_occurrences(input_string):
    words = input_string.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
