"""
Printing is nice for debugging, but most functions need to give back a result.
A function that calculates tax should return the amount.
A function that finds a user should return the user object. That's what return does.

Returning Different Types - Python doesn't restrict what you return, but be consistent
"""


# return sends a value back to the caller.
def add(a, b):
    return a + b


result = add(3, 5)
print(result)


# Basic Return
def square(n):
    return n ** 2


result = square(4)
print(result)

# Use it directly in expressions
print(square(3) + square(4))


# Functions Without Return - Functions without return return None:
# This is fine for functions that perform actions (print, save, send) rather than compute values.
def greet(name):
    print(f"Hello, {name}!")


result = greet("Alice")
print(result)


# Early Return - return immediately exits the function:
# Use early returns to handle edge cases at the top
def divide(a, b):
    if b == 0:
        return None  # Exit early
    return a / b


print(divide(10, 2))
print(divide(10, 0))


# Returning Multiple Values - Return multiple values with a tuple:
def get_dimensions():
    return 1920, 1080  # Returns a tuple


# Unpack the result
width, height = get_dimensions()
print(width)
print(height)

# Or keep as tuple
dimensions = get_dimensions()
print(dimensions)


# Returning Collections
def get_even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


evens = get_even_numbers([1, 2, 3, 4, 5, 6])
print(evens)
