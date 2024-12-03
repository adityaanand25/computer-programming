Partition a list into sublists of equal length
def partition_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(partition_list(lst, 3))
