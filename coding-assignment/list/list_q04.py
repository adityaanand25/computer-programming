Find the longest increasing subsequence in a list
def longest_increasing_subsequence(lst):
    if not lst:
        return []
    dp = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    max_length = max(dp)
    sequence = []
    for i in range(len(lst) - 1, -1, -1):
        if dp[i] == max_length:
            sequence.append(lst[i])
            max_length -= 1
    return sequence[::-1]
lst = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(lst))
