#You have a list of items and want to categorize them into a dictionary based on their first letter.
python

items = ['apple', 'banana', 'apricot', 'blueberry']
categorized = {}
for item in items:
    key = item[0]
    if key not in categorized:
        categorized[key] = []
    categorized[key].append(item)
print(categorized)
