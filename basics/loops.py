"""
Topic: Loops
Example: Space Mission Launch Sequence

This file demonstrates how loops can
repeat tasks in Python.
"""

print("====== Mission Control ======")
print("Initializing launch sequence...")
print()

# Get the number of systems
number_of_systems = int(input("Enter number of systems to check: "))

print()

# Check each system
for system in range(1, number_of_systems + 1):
    print("Checking system", system, "... OK")

print()

# Get countdown number
countdown = int(input("Enter countdown starting number: "))

print()
print("Starting countdown...")
print()

# Countdown
for number in range(countdown, 0, -1):
    print(number, "...")

print()
print("🚀 Liftoff!")
