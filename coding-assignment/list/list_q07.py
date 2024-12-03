Find the product of all elements except the current element in a list
def product_except_self(lst):
    n = len(lst)
    left, right, result = [1] * n, [1] * n, [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * lst[i - 1]
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * lst[i + 1]
    for i in range(n):
        result[i] = left[i] * right[i]
    return result
lst = [1, 2, 3, 4]
print(product_except_self(lst))
