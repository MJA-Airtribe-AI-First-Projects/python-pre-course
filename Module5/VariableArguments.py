"""
Sometimes you don't know how many arguments a function will receive.
A sum function might take 2 numbers or 20.
A format function might receive various options.
Python's *args and **kwargs let you handle any number of arguments flexibly.

Order matters: regular parameters, then *args, then **kwargs
Naming Convention: args and kwargs are just conventions. You can use any names
"""


# *args — any number of positional arguments
def add_all(*args):
    return sum(args)


print(add_all(1, 2))
print(add_all(1, 2, 3, 4, 5))


# **kwargs — any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30)


# *args: Variable Positional Arguments - The * collects extra positional arguments into a tuple
def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")


greet_all("Alice")
greet_all("Alice", "Bob", "Charlie")


# *args With Regular Parameters - You can mix regular parameters with *args:
def make_sentence(subject, *words):
    return f"{subject} {' '.join(words)}"


print(make_sentence("Python", "is", "awesome"))
print(make_sentence("I", "love", "writing", "code"))


# **kwargs: Variable Keyword Arguments - The ** collects extra keyword arguments into a dictionary:
def build_profile(**kwargs):
    return kwargs


profile = build_profile(name="Alice", age=30, city="NYC")
print(profile)


# **kwargs With Regular Parameters
def create_user(username, email, **extra):
    user = {
        "username": username,
        "email": email
    }
    user.update(extra)  # Add any extra fields
    return user


user = create_user(
    "alice",
    "alice@example.com",
    age=30,
    role="admin",
    department="Engineering"
)
print(user)


# Combining *args and **kwargs - Use both to accept any combination of arguments:
def flexible(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")


flexible(1, 2, 3, name="Alice", active=True)

# Unpacking: The Other Direction - You can also use * and ** when calling functions:

# Unpacking Lists/Tuples with *
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))

# Without unpacking:
# print(add(numbers))  # Error! Passes list as single argument

# Unpacking Dictionaries with **
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

options = {"name": "Alice", "greeting": "Hi"}
greet(**options)
