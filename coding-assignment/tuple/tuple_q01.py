 Flatten a Nested Tuple

def flatten_tuple(nested_tup):
    flat_list = []
    def flatten(tup):
        for item in tup:
            if isinstance(item, tuple):
                flatten(item)
            else:
                flat_list.append(item)
    flatten(nested_tup)
    return tuple(flat_list)

result = flatten_tuple(((1, 2), (3, (4, 5))))
print(result)  # Output: (1, 2, 3, 4, 5)
