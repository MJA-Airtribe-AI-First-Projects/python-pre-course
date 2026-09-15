"""
Logical Operators - and, or, not
Sometimes one condition isn't enough. You need a way to combine conditions. That's what logical operators do.

Truth table for and:
True and True    # True
True and False   # False
False and True   # False
False and False  # False

Truth table for or:
True or True    # True
True or False   # True
False or True   # True
False or False  # False

Python stops evaluating as soon as it knows the answer:

With and: If the first condition is False, Python doesn't check the rest:

is_logged_in = False

# expensive_check() never runs!
if is_logged_in and expensive_check():
    ...

With or: If the first condition is True, Python doesn't check the rest:

is_admin = True

# expensive_check() never runs!
if is_admin or expensive_check():
    ...
"""

# and - both must be True
is_logged_in = True
is_premium = True
if is_logged_in and is_premium:
    print("show_premium_content")

# or - at least one must be True
is_admin = is_moderator = True
if is_admin or is_moderator:
    can_delete = True

# not - flips True to False
is_banned = True
if not is_banned:
    print("allow_access")

# not flips a boolean:
print(not True)  # False
print(not False)  # True

# Combining Operators
age = 25
is_student = True
is_senior = False

# Must be adult AND (student OR senior)
gets_discount = age >= 18 and (is_student or is_senior)
print(gets_discount)

"""
Order of Operations
Python evaluates in this order:
1. not (first)
2. and
3. or (last)
"""

# Without parentheses
print(True or False and False)
# Python reads: True or (False and False)

# With parentheses - different result
print((True or False) and False)

# Range Check
age = 25

# Verbose way
if 18 <= age <= 65:
    print("Working age")

# Pythonic way
if 18 <= age <= 65:
    print("Working age")

# Check Against Multiple Values
day = "Saturday"

# Verbose way
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

# Pythonic way (we'll cover `in` later)
if day in ("Saturday", "Sunday"):
    print("Weekend!")

# Default Values with or
username = ""
display_name = username or "Guest"
print(display_name)  # "Guest"

username = "Alex"
display_name = username or "Guest"
print(display_name)  # "Alex"
