"""
Sets automatically handle uniqueness.
Sets are unordered, items don't have positions.
They're also mutable, you can add and remove items.
"""

# Create a set
tags = {"python", "django", "web"}

# No duplicates
tags.add("python")  # Already exists, set unchanged
print(tags)

# Fast membership check
print("python" in tags)

# Sets use curly braces {} to create, but without key-value pairs:
# Set of strings
colors = {"red", "green", "blue"}

# From a list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)
print(unique)

# Empty set (not {} — that's an empty dict!)
empty = set()

# No Duplicates
tags = {"python", "web", "python", "api", "web"}
print(tags)

# Unordered
# You can't do colors[0],sets don't support indexing
# Order may vary when you print
colors1 = {"red", "green", "blue"}
print(colors1)

# Fast Membership Testing
# Checking "in" is O(1) — very fast
large_set = set(range(1_000_000))
print(999_999 in large_set)  # Nearly instant

# Modifying Sets
tags = {"python", "django"}

# Add one item
tags.add("web")
print(tags)

# Add multiple items
tags.update(["api", "rest"])
print(tags)

# Remove an item (raises error if not found)
tags.remove("web")
print(tags)

# Remove an item (no error if not found)
tags.discard("nonexistent")
print(tags)

# Remove and return an arbitrary item
item = tags.pop()
print(item)

# Set Operations
s1 = {1, 2, 3}
s2 = {3, 4, 5, 6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

# Set Comparisons
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2, 3}

# Subset — all items of a are in b
print(a <= b)
print(a.issubset(b))

# Proper subset — subset but not equal
print(a < b)
print(a < c)

# Superset — b contains all items of a
print(b >= a)
print(b.issuperset(a))

# Disjoint — no items in common
print({1, 2}.isdisjoint({3, 4}))
print({1, 2}.isdisjoint({2, 3}))

# Frozen Sets - Need an immutable set? Use frozenset:
# Immutable — can't add or remove
immutable = frozenset([1, 2, 3])
# immutable.add(4) # This will throw an error
