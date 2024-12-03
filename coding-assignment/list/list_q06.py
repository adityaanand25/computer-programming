Find the kth smallest element in a list using Quickselect
def quickselect(lst, k):
    if lst:
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        mid = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        if k < len(left):
            return quickselect(left, k)
        elif k < len(left) + len(mid):
            return mid[0]
        else:
            return quickselect(right, k - len(left) - len(mid))
lst = [3, 2, 1, 5, 4]
print(quickselect(lst, 2))
