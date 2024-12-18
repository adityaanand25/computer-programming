Question: Move all spaces to the front of the string.

def move_spaces_to_front(input_string):
    spaces = ''.join(filter(lambda x: x == ' ', input_string))
    non_spaces = ''.join(filter(lambda x: x != ' ', input_string))
    return spaces + non_spaces
