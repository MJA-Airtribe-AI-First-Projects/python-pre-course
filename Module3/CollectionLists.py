"""
List store multiple values together.
List can have any type of data.

1. Lists use square brackets: ["a", "b", "c"]
2. Zero-indexed: first item is at index 0
3. Mutable: can add, remove, and change items
4. Negative indices count from the end: list[-1] is the last item
5. in checks membership: "x" in list
6. append() adds to the end, insert() adds at a position
7. sort() modifies in place, sorted() returns a new list
"""

# Create a list
fruits = ["apple", "banana", "cherry"]

# Access items by index (starts at 0)
print(fruits[0])  # "apple"

# Add an item
fruits.append("orange")

# Lists are mutable — you can change them
fruits[1] = "blueberry"
print(fruits)

# List of strings
colors = ["red", "green", "blue"]

# List of numbers
prices = [10.99, 24.50, 5.00]

# Mixed types (allowed, but usually not a good idea)
mixed = ["hello", 42, True]

# Empty list
empty = []

# Accessing Items - Lists are zero-indexed, the first item is at position 0:
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])

# Modifying Lists - Lists are mutable, you can change them after creation:
fruits = ["apple", "banana", "cherry"]
fruits[0] = "apricot"
print(fruits)

# Add to the end
fruits.append("date")
print(fruits)

# Insert at a specific position
fruits.insert(1, "blueberry")
print(fruits)

# Removing Items
fruits = ["apple", "banana", "cherry", "banana"]

# Remove by value (first occurrence only)
fruits.remove("banana")
print(fruits)

# Remove by index
del fruits[0]
print(fruits)

# Remove and return the last item
last = fruits.pop()
print(last)
print(fruits)

# Remove and return item at specific index
fruits = ["apple", "banana", "cherry"]
item = fruits.pop(1)
print(item)

# List Length and Membership
fruits = ["apple", "banana", "cherry"]

# Length
print(len(fruits))

# Check if item exists
print("banana" in fruits)
print("mango" in fruits)
print("mango" not in fruits)

# Slicing Lists - Get a portion of a list:
letters = ["a", "b", "c", "d", "e"]

print(letters[1:4])
print(letters[:3])
print(letters[2:])
print(letters[::2])
print(letters[::-1])

# Common List Operations
numbers = [3, 1, 4, 1, 5, 9]

# Sort (modifies the original list)
numbers.sort()
print(numbers)

# Reverse
numbers.reverse()
print(numbers)

# Get a sorted copy (original unchanged)
original = [3, 1, 4]
sorted_copy = sorted(original)
print(original)
print(sorted_copy)

# Count occurrences
numbers = [1, 2, 2, 3, 2, 2]
print(numbers.count(2))

# Find index
print(numbers.index(3))

# Combining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenate - + creates a new list
combined = list1 + list2
print(combined)

# Extend (modifies list1) - extend() modifies in place
list1.extend(list2)
print(list1)
