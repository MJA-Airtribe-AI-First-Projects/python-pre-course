"""
A variable is a name that points to a value.

Naming Variables:
- The Rules (Python enforces these)
    1. Start with a letter or underscore
    2. Only letters, numbers, and underscores
    3. Can't use Python keywords (if, for, class, etc.)

The = Sign, means "assign the value on the right to the name on the left."
x = 5
Read this as: "x becomes 5."

The Conventions (Pythonistas follow these)
- Python uses snake_case - lowercase words separated by underscores:
    Ex: user_email = "alex@example.com"
"""

# Creating Variables
name = "Alex"  # string
age = 25  # integer
price = 19.99  # float
is_student = True  # boolean

# Assigning Value to Variable and Perform Addition.
x = 5
x = x + 1
print(x)

# When you're updating a variable based on its current value, Python offers shortcuts:
count = 10

# These are the same:
count = count + 1
count += 1

# Works with other operators too:
count -= 5  # Same as count = count - 5
count *= 2  # Same as count = count * 2
count /= 4  # Same as count = count / 4

"""
Constants (By Convention)
Sometimes you have values that shouldn't change, like configuration settings or fixed rates.
Python doesn't have true constants. Nothing stops you from changing these. The ALL_CAPS naming is a convention that signals "don't change this."
"""

MAX_UPLOAD_SIZE = 10485760  # 10 MB in bytes
TAX_RATE = 0.18
API_VERSION = "v2"

# A Handy Trick: Multiple Assignment
# Assign same value to multiple variables
x = y = z = 0

# Assign different values in one line
name1, age1, city = "Alex", 25, "Mumbai"
print(name1, age1, city)

# Swap values without a temp variable
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1
