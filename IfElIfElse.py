"""
if statements, lets your program take different paths based on conditions.
"""

age = 20

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")

# If-Elif-Else: Multiple Paths
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)

# Order Matters - The conditions are checked in order, and only the first match runs:
age = 25

# Wrong order - "Adult" never prints!
if age >= 0:
    print("Alive")  # This runs (25 >= 0)
elif age >= 18:
    print("Adult")  # Never reached
elif age >= 65:
    print("Senior")  # Never reached

# Nested If Statements - You can put if statements inside other if statements:
is_member = True
cart_total = 150

if is_member:
    if cart_total >= 100:
        print("Free shipping!")
    else:
        print("$5 shipping")
else:
    if cart_total >= 200:
        print("Free shipping!")
    else:
        print("$10 shipping")

# Multiple Independent Checks - Sometimes you need to check several things independently - not either/or:
temperature = 25
is_raining = True

# These are independent checks, not alternatives
if temperature > 30:
    print("Bring water")

if is_raining:
    print("Bring umbrella")

if temperature < 10:
    print("Bring jacket")

"""
Common Patterns
Guard Clause (Early Exit)
Check for invalid cases first:
"""

def process_order(user, items):
    if not user:
        return "Please log in"

    if not items:
        return "Cart is empty"

    # Main logic here...
    return "Order processed"

# Short way (ternary expression)
status = "adult" if age >= 18 else "minor"

