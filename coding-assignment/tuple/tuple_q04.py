def rotate_tuple(tup, k):
    k = k % len(tup) if tup else 0
    return tup[-k:] + tup[:-k]
result = rotate_tuple((1, 2, 3, 4), k=2)
print(result)  # Output: (3, 4, 1, 2)
