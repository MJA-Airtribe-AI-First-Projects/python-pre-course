"""
Basic parameters work, but real code needs more flexibility. What if some values are optional? What if you want to be explicit about which argument is which? Python's parameter system handles all of this.

Parameters vs Arguments
- Quick terminology:
    1. Parameters: Variables in the function definition
    2. Arguments: Values passed when calling the function
"""


# Parameters can have defaults, and arguments can be passed by name.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")
greet("Bob", "Hi")
greet(greeting="Hey", name="Charlie")


def add(a, b):  # a and b are parameters
    return a + b


result = add(3, 5)  # 3 and 5 are arguments


# Positional Arguments - Arguments matched by position:
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")


describe_pet("dog", "Rex")
describe_pet("Rex", "dog")


# Keyword Arguments - Arguments matched by name:
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")


describe_pet(animal="dog", name="Rex")
describe_pet(name="Rex", animal="dog")


# Mixing Positional and Keyword - You can use both, but positional must come first:
def create_user(username, email, role="user"):
    print(f"Creating {role}: {username} ({email})")


# All valid
create_user("alice", "alice@example.com")
create_user("bob", "bob@example.com", "admin")
create_user("charlie", email="charlie@example.com")
create_user("diana", "diana@example.com", role="moderator")


# Default Parameter Values - Make parameters optional with defaults:
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")


greet("Alice")
greet("Bob", "Hi")
greet("Charlie", "Hey", "?")
greet("Diana", punctuation="...")


# The Mutable Default Gotcha - Never use a mutable object as a default value:
# DON'T DO THIS
def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("a"))
print(add_item("b"))


# Required vs Optional Parameters
def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
    """
    Send an email.

    Required: to, subject, body
    Optional: cc, bcc, priority
    """
    print(f"Sending to {to}: {subject}")
    if cc:
        print(f"  CC: {cc}")
    if bcc:
        print(f"  BCC: {bcc}")
    print(f"  Priority: {priority}")


# Minimal call
send_email("bob@example.com", "Hello", "Message body")

# With options
send_email(
    "bob@example.com",
    "Urgent",
    "Please respond",
    priority="high"
)
