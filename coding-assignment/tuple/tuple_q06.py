 Find the Second Largest Element in a Tuple
def second_largest(tup):
    unique_elements = set(tup)
    if len(unique_elements) < 2:
        return None
    unique_elements.remove(max(unique_elements))
    return max(unique_elements)

result = second_largest((1, 2, 3, 4, 5))
print(result)
