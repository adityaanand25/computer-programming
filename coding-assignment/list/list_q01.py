Write a program to rotate a list by k positions to the right

Copy code
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
lst = [1, 2, 3, 4, 5, 6]
print(rotate_list(lst, 2))
