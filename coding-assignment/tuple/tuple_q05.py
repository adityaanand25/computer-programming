def compare_tuples(tup1, tup2):
    if tup1 < tup2:
        return -1
    elif tup1 > tup2:
        return 1
    else:
        return 0

result = compare_tuples((1,2), (1,3))
print(result)  
result = compare_tuples((1,), (1,))
print(result)  
result = compare_tuples((2,), (1,))
print(result)  
