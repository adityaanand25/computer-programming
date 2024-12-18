 Create a Tuple of Squares
def tuple_of_squares(n):
    return tuple(i**2 for i in range(n))
result = tuple_of_squares(5)
print(result)
