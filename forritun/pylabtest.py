def my_function(start, other=[]):
    if start in other:
        return None
    other.append(start)
    return start

print(my_function(other=[], start=5))
print(my_function(5))