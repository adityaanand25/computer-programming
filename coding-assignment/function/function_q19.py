 Write a Python program to detect the number of local variables declared in a function.

def count_local_vars():
    x = 10
    y = "Hello"
    z = [1, 2, 3]
    return len(locals())
print(count_local_vars())
