"""
Every program takes input, processes it, and produces output. Let's learn how Python handles the input and output parts.
"""

# Output - display something
print("Hello!")

# Input - get something from user
name = input("What's your name? ")

# Format strings nicely with f-strings
print(f"Hello, {name}!")

# Print multiple things with commas (Python adds spaces):
name = "Dhaval"
age = 30
print("Name:", name, "Age:", age)

# Escape Characters - Special characters in strings:
# Newline - starts a new line
print("Line 1\nLine 2")
# Tab - adds horizontal spacing
print("Name:\tAlex")
# Backslash - when you need a literal \
print("C:\\Users\\Alex")
# Quote inside same quote type
print("She said \"hello\"")

# Customizing print()
# Change separator (default is space)
print("2024", "01", "15", sep="-")
# Change ending (default is newline)
print("Loading", end="...")
print("Done!")

# Combine both
print("a", "b", "c", sep=", ", end="!\n")

# Important: input() Always Returns a String. Even if the user types a number:

age = input("Enter your age: ")
print(type(age))  # <class 'str'>

# String Formatting
name = "Dhaval"
balance = 100.50
message = f"Hello, {name}! Your balance is ${balance}"
print(message)

# Do Math Inside
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")

# Call Methods
name = "alex"
print(f"Hello, {name.upper()}!")

# Format Numbers
# Two decimal places
price = 19.5
print(f"${price:.2f}")

# Add commas for thousands
population = 7900000000
print(f"{population:,}")

# Percentages
rate = 0.756
print(f"{rate:.1%}")

# Other Formatting Methods (For Reference)
# .format() method
message = "Hello, {}! Balance: ${:.2f}".format(name, balance)
print(message)

# %-formatting (oldest)
message1 = "Hello, %s! Balance: $%.2f" % (name, balance)
print(message1)

# A simple registration flow:
print("=== Sign Up ===")
username = input("Choose a username: ")
email = input("Your email: ")
age = int(input("Your age: "))

years_to_100 = 100 - age

print()
print(f"Welcome, {username}!")
print(f"Confirmation sent to: {email}")
print(f"Fun fact: You'll be 100 in {years_to_100} years!")
