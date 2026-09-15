"""
Functions let you write code once and use it many times.
They make your code organized, readable, and easier to test.

Function Naming Conventions: Python uses snake_case for function names:
"""


def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
greet("Bob")

"""
Basic Function Structure

Key parts:
1. def keyword starts the definition
2. Function name (follows same rules as variables)
3. Parentheses () (may contain parameters)
4. Colon : ends the definition line
5. Indented body (the code that runs)
"""


def function_name():
    # Code goes here
    print("This is a function")


# Call the function
function_name()


# Functions With Parameters - Most functions need input to be useful:
def greet(name):
    print(f"Hello, {name}!")


def square(number):
    print(number ** 2)


greet("Alice")
square(5)


# Docstrings - Documenting Functions - Add documentation with a docstring:
# Docstrings appear when you use help(calculate_area) and in IDE tooltips.
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle
        height: The height of the rectangle

    Returns:
        The area (width * height)
    """
    return width * height


print(calculate_area(10, 12))


# Functions Are Objects - In Python, functions are objects you can assign them to variables:
def shout(text):
    return text.upper()


# Assign function to variable (no parentheses)
yell = shout

# Call through the new name
print(yell("hello"))


# Pass functions to other functions
def apply_twice(func, value):
    return func(func(value))


print(apply_twice(shout, "hi"))
