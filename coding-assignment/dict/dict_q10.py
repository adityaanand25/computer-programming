#Given a dictionary of products with prices, extract all products that are above a certain price threshold into a new dictionary.

products = {'apple': 2.5, 'banana': 1.5, 'cherry': 3.0}
threshold = 2.0
expensive_products = {k: v for k, v in products.items() if v > threshold}
print(expensive_products)
