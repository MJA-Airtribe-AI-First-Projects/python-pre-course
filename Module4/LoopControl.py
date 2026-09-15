"""
Basic loops run from start to finish. But sometimes you need more control.
Stop searching once you've found what you need.
Skip invalid items but keep processing the rest.
Do something only if the loop completed without finding what it was looking for.
That's what break, continue, and loop else are for.
"""

# break — exit the loop immediately
for n in range(10):
    if n == 5:
        break  # Stop here
    print(n)  # 0, 1, 2, 3, 4

# continue — skip to next iteration
for n in range(5):
    if n == 2:
        continue  # Skip this one
    print(n)  # 0, 1, 3, 4

# else — runs if loop completed without break
for n in range(3):
    print(n)
else:
    print("Loop finished!")  # This runs

# Break: Exit Early - break immediately exits the loop:
# Find the first even number
numbers = [1, 3, 5, 8, 9, 12]

for n in numbers:
    if n % 2 == 0:
        print(f"Found even number: {n}")
        break

# Continue: Skip This Iteration - continue skips to the next iteration without exiting the loop:
# Process only valid items
data = [10, -5, 20, None, 30, "invalid"]

for item in data:
    if not isinstance(item, int) or item < 0:
        continue  # Skip invalid items

    print(f"Processing: {item}")

"""
The Loop Else Clause
Python has a unique feature: else on loops. It runs only if the loop completes without hitting break:
"""
# Search for a user
users = ["alice", "bob", "charlie"]
target = "david"

for user in users:
    if user == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")


# Practical Example: Validation
def validate_passwords(passwords):
    for password in passwords:
        if len(password) < 8:
            print(f"Invalid: {password} is too short")
            break
    else:
        print("All passwords are valid!")
        return True
    return False


# Test
validate_passwords(["secure123", "mypassword", "hello"])
validate_passwords(["secure123", "mypassword", "verysafe1"])

# Nested Loops and Break - break only exits the innermost loop:
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only exits inner loop
        print(f"i={i}, j={j}")
    print(f"Finished inner loop for i={i}")
