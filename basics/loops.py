"""
Topic: Loops
Example: Space Mission System Check

This file demonstrates how a for loop
can repeat tasks in Python.
"""

print("===== Mission Control =====")
print("Initializing system check...")
print()

# Get the number of systems
number_of_systems = int(input("Enter number of systems to check: "))

print()

# Check each system
for system in range(1, number_of_systems + 1):
    print("Checking system", system, "... OK")

print()
print("✅ All systems are ready!")
print("🚀 Liftoff!")
