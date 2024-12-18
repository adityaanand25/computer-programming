Question: Capitalize the first letter of each word in a string.

def capitalize_first_letter(input_string):
    return " ".join(word.capitalize() for word in input_string.split())
