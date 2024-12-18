Question: Remove duplicate characters from a string while maintaining order.

def remove_duplicates(input_string):
    return "".join(sorted(set(input_string), key=input_string.index))
