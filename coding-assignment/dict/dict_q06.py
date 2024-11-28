#Given a list with duplicates, use a dictionary to remove duplicates while maintaining order.

items = ['apple', 'banana', 'apple', 'orange']
unique_items = {}
for item in items:
    unique_items[item] = None
print(list(unique_items.keys()))
