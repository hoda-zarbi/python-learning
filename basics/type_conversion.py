"""
Topic: Type Conversion
Example: Laptop Registration Form

This file demonstrates how to convert user input
from strings into different data types in Python.
"""

print("=== Laptop Registration Form ===")
print()

# Receive laptop information From the user
model = input("Enter the laptop model: ")
ram = int(input("Enter the RAM size (GB): "))
storage = int(input("Enter the storage size (GB): "))
price = float(input("Enter the price ($): "))

print()

# Display the laptop information
print("==== Laptop Specifications ====")
print("Model:", model)
print("RAM:", ram, "GB")
print("Storage:", storage, "GB")
print("Price: $", price)
