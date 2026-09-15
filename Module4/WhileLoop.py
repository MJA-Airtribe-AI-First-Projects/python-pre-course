"""
When you need to repeat based on a condition rather than a collection, use a while loop.
While loops are great for consuming queues or stacks
"""

count = 0

while count < 5:
    print(count)
    count += 1

"""
Basic While Loop

How it works:
1. Check condition: Is balance > 0?
2. If yes, run the body
3. Go back to step 1
4. If no, exit the loop
"""
balance = 100

while balance > 0:
    withdrawal = 30
    balance -= withdrawal
    print(f"Balance: {balance}")

# Processing Until Empty

tasks = ["email", "backup", "report"]

while tasks:  # Non-empty list is truthy
    current = tasks.pop(0)  # Remove first item
    print(f"Processing: {current}")

print("All tasks complete!")

# Infinite Loops (On Purpose) - Sometimes you want a loop that runs forever like a server:
# Conceptual example — don't actually run this
# while True:
#     request = wait_for_request()
#     response = handle_request(request)
#     send_response(response)

# Infinite Loops (By Accident)
# DON'T DO THIS — infinite loop!
# count = 0
# while count < 5:
#     print(count)
# Forgot to increment count!
