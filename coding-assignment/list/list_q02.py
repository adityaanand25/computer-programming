Find all unique triplets in a list that sum up to a target value

def three_sum(lst, target):
    lst.sort()
    result = []
    for i in range(len(lst) - 2):
        if i > 0 and lst[i] == lst[i - 1]:
            continue
        left, right = i + 1, len(lst) - 1
        while left < right:
            total = lst[i] + lst[left] + lst[right]
            if total == target:
                result.append([lst[i], lst[left], lst[right]])
                left += 1
                right -= 1
                while left < right and lst[left] == lst[left - 1]:
                    left += 1
                while left < right and lst[right] == lst[right + 1]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return result
print(three_sum([1, 2, -1, -1, -2, 3, 4], 2))
