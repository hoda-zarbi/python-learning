"""
Topic: Conditional Statements
Example: Weather Clothing Advisor

This file demonstrates how conditional statements
can be used to make decisions in Python.
"""

print("=== Weather Clothing Advisor ===")
print()

# Receive weather information from the user
temperature = float(input("Enter the temperature (°C): "))

print()

# Recommend clothing based on the temperature
if temperature < 10:
    print("Recommendation: Wear a warm winter coat.")

elif temperature < 20:
    print("Recommendation: Wear a light jacket.")

elif temperature < 30:
    print("Recommendation: A T-shirt is a good choice.")

else:
    print("Recommendation: Wear light clothes and stay hydrated.")
