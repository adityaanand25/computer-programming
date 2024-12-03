Flatten a deeply nested list

def flatten_list(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flat.extend(flatten_list(i))
        else:
            flat.append(i)
    return flat
nested_list = [1, [2, [3, [4, 5]], 6], 7]
print(flatten_list(nested_list))
