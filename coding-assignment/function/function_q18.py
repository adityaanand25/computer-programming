Write a Python program to access a function inside another function.

def outer_function():
    def inner_function():
        return "Hello from inner function!"
    return inner_function()
print(outer_function())
