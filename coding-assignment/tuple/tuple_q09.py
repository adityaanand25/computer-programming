 Check if a Tuple is a Subset of Another Tuple
def is_subset(tup1, tup2):
    return set(tup1).issubset(set(tup2))

result = is_subset((1, 2), (1, 2, 3))
print(result) 
