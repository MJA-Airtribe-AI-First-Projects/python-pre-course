"""
Not all data is the same. A user's name is text. Their age is a number. Whether they're logged in is a yes/no.
Python needs to know what type of data it's working with because different types behave differently.

1. str - text in quotes
2. int - whole numbers
3. float - decimal numbers
4. bool - True or False
5. None - absence of value
6. Use type() to check, int(), str(), float() to convert
7. User input is typically a string - convert when needed
"""

name = "Alex"  # str (string) - text
age = 25  # int (integer) - whole number
price = 19.99  # float - decimal number
is_active = True  # bool (boolean) - True or False
middle_name = None  # NoneType - "no value"

# Common String Operations

name1 = "  Alex Smith  "
name1.lower()  # "  alex smith  "
name1.upper()  # "  ALEX SMITH  "
name1.strip()  # "Alex Smith" (removes whitespace)
name1.replace("Smith", "Jones")  # "  Alex Jones  "
email = "user@example.com"
email.startswith("user")  # True
email.endswith(".com")  # True
print("@" in email)  # True

# Numbers in quotes are strings, not numbers:

a = 100  # Integer
b = "100"  # String
print(a + a)  # 200 (math)
print(b + b)  # "100100" (text joined together)

# Checking Types
print(type("hello"))  # <class 'str'>
print(type(42))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>

# Checking Specific Types
isinstance(age, int)  # True
isinstance(age, str)  # False
isinstance(name, str)  # True

# Check multiple types at once
isinstance(age, (int, float))  # True, age is one of these types

# Converting Between Types
age_str = "25"
age_num = int(age_str)  # Now it's the number 25

# Integer to string
count = 10
count_str = str(count)  # Now it's "10"

# String to float
price_str = "19.99"
price_num = float(price_str)  # Now it's 19.99
