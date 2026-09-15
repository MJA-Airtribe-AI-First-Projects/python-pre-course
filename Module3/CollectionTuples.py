"""
Lists are great, but sometimes you want data that can't be changed. Coordinates that shouldn't move. Configuration values that should stay constant. Database records that represent a fixed snapshot. That's where tuples come in.
"""

# Create a tuple
point = (10, 20)

# Access items (same as lists)
print(point[0])

# Tuples are immutable — this would error:
# point[0] = 15  # TypeError!

# Creating Tuples - Tuples use parentheses ()
# Tuple of coordinates
point = (10, 20)
print(point)

# Tuple of strings
colors = ("red", "green", "blue")
print(colors)

# Single-item tuple needs a trailing comma
single = (42,)  # This is a tuple
print(type(single))
not_tuple = (42)  # This is just the number 42
print(type(not_tuple))

# You can omit parentheses (tuple packing)
coordinates = 10, 20, 30
print(type(coordinates))  # <class 'tuple'>

# Accessing Items - Works exactly like lists:
colors = ("red", "green", "blue")

print(colors[0])
print(colors[-1])
print(colors[1:3])

# Tuples Are Immutable - You can't change a tuple after creation:
point = (10, 20)

# These all raise TypeError:
# point[0] = 15  # Can't change items
# point.append(30)  # No append method
# point.remove(10)  # No remove method

"""
The tuple itself is immutable, you can't replace data[2] with a different object. 
But the list inside the tuple is still mutable. 
You can't reassign data[2] = something_else, but you can modify the existing list.
"""
data = (1, 2, [3, 4])
data[2].append(5)
print(data)

# Tuple Unpacking
point1 = (10, 20)
x, y = point1
print(x)  # 10
print(y)  # 20

# Extended Unpacking - Use * to capture multiple values:
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers
print(first)
print(middle)
print(last)

head, *tail = numbers
print(head)
print(tail)
