"""
When you want to look up a user's email by their username, or get a product's price by its ID, you need dictionaries.
"""

# Create a dictionary
user = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30
}

# Access by key
print(user["name"])  # "Alice"

# Add or update
user["role"] = "admin"
user["age"] = 31
print(user)

# Creating Dictionaries - Dictionaries use curly braces {} with key-value pairs:
# String keys (most common)
user = {
    "username": "alice",
    "email": "alice@example.com"
}
print(user)

# Integer keys
http_codes = {
    200: "OK",
    404: "Not Found",
    500: "Server Error"
}
print(http_codes)

# Empty dictionary
empty = {}

# From a list of tuples
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print(d)

# Accessing Values - Use square brackets with the key:
user = {"name": "Alice", "age": 30}

print(user["name"])
print(user["age"])
# print(user["email"])  # KeyError! Key doesn't exist

# Safe Access with .get()
# Returns None if key doesn't exist
print(user.get("email"))

# Or specify a default value
print(user.get("email", "not provided"))
print(user.get("name", "not provided"))

# Modifying Dictionaries
user = {"name": "Alice"}

# Add a new key
user["email"] = "alice@example.com"
print(user)

# Update existing key
user["name"] = "Alice Smith"
print(user)

# Delete a key
del user["email"]
print(user)

# Remove and return a value
name = user.pop("name")
print(name)

# pop with default (no error if missing)
role = user.pop("role", "guest")

# Iterating Over Dictionaries
user = {"name": "Alice", "age": 30, "role": "admin"}

# Iterate over keys (default)
for key in user:
    print(key)  # name, age, role

# Iterate over values
for value in user.values():
    print(value)  # Alice, 30, admin

# Iterate over both
for key, value in user.items():
    print(f"{key}: {value}")

# Common Operations
user = {"name": "Alice", "age": 30}

# Get all keys
print(list(user.keys()))

# Get all values
print(list(user.values()))

# Get key-value pairs as tuples
print(list(user.items()))

# Number of keys
print(len(user))

# Merge dictionaries
defaults = {"role": "user", "active": True}
user.update(defaults)
print(user)

# Python 3.9+ merge syntax
defaults = {"role": "user1", "active": False}
merged = user | defaults
print(merged)

# Nested Dictionaries
users = {
    "alice": {
        "email": "alice@example.com",
        "age": 30
    },
    "bob": {
        "email": "bob@example.com",
        "age": 25
    }
}

# Access nested values
print(users["alice"]["email"])

# Safe nested access
print(users.get("charlie", {}).get("email", "N/A"))
