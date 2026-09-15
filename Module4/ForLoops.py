"""
Iterating Over Collections.
"""

users = ["alice", "bob", "charlie"]

for user in users:
    print(f"Hello, {user}!")

"""
Basic For Loop

How it works:
1. First iteration: color = "red", print it
2. Second iteration: color = "green", print it
3. Third iteration: color = "blue", print it
4. No more items, loop ends
"""
colors = ["red", "green", "blue"]

for color in colors:
    print(color)

# Looping Over Different Types
# List
prices = [10.99, 24.50, 5.00]
total = 0

for price in prices:
    total += price

print(total)

# String
word = "Python"

for char in word:
    print(char)

# Dictionaries
user = {"name": "Alice", "age": 30, "role": "admin"}

# Loop over keys (default)
for key in user:
    print(key)  # name, age, role

# Loop over values
for value in user.values():
    print(value)  # Alice, 30, admin

# Loop over both
for key, value in user.items():
    print(f"{key}: {value}")

# The range() Function - range(start, stop, step) - stop is excluded, just like slicing.
# 0 to 4 (5 times)
for i in range(5):
    print(i)

# 1 to 5
for i in range(1, 6):
    print(i)

# 0, 2, 4, 6, 8 (step of 2)
for i in range(0, 10, 2):
    print(i)

# Countdown: 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i)

# Getting the Index with enumerate() - Sometimes you need both the item and its position:
fruits = ["apple", "banana", "cherry"]

# Without enumerate (works but clunky)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (cleaner)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start from a different number
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")

# Looping Over Multiple Lists with zip()
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Nested Loops - Loops inside loops:
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")

# Building New Lists - A common pattern, process items and collect results:
numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)
