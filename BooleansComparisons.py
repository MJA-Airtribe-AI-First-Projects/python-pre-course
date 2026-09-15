"""
Every decision comes down to a yes-or-no question and Python answers those with booleans.

Truthy and Falsy: Python treats some non-boolean values as "sort of true" or "sort of false."

- Falsy values (act like False):
    1. False
    2. None
    3. 0 (zero)
    4. "" (empty string)
    5. [] (empty list)
    6. {} (empty dictionary)
- Truthy values (act like True):
    1. Everything else
"""

# Booleans: True or False
is_logged_in = True
is_admin = False

# Comparisons produce booleans
age = 25
print(age >= 18)  # True
print(age == 30)  # False

# Comparison Operators
age = 25
print(age == 25)  # True
print(age != 30)  # True
print(age > 18)  # True
print(age < 18)  # False
print(age >= 25)  # True

# Common Mistake: = vs ==
x = 5  # Assignment: x becomes 5
print(x == 5)  # Comparison: is x equal to 5? (returns True)

# Comparing Strings
# String comparison is case-sensitive:
name = "Alice"

print(name == "Alice")  # True
print(name == "alice")  # False (different case)
print(name == "Bob")  # False

# Storing Comparison Results
age = 25
minimum_age = 18

is_adult = age >= minimum_age
print(is_adult)  # True

# More readable than putting the comparison inline
if is_adult:
    print("Access granted")

# The bool() Function - Convert any value to a boolean explicitly:
bool(0)  # False
bool(42)  # True
bool("")  # False
bool("hello")  # True
bool([])  # False
bool([1, 2])  # True
bool(None)  # False
