 Find Unique Elements Across Multiple Tuples
def unique_elements(*tuples):
    unique_set = set()
    for tup in tuples:
        unique_set.update(tup)
    return tuple(unique_set)

result = unique_elements((1, 2, 3), (3, 4), (4, 5))
print(result)  # Output: (1, 2, 3, 4, 5)
