 Find the Frequency of Elements in a Tuple

def frequency_of_elements(tup):
    frequency = {}
    for item in tup:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

result = frequency_of_elements((1, 2, 2, 3, 3, 3))
print(result)
