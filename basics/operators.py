"""
Topic: Operators
Example: Online Store Checkout

This file demonstrates how arithmetic operators perform
basic calculations in Python.
"""

print("=== Online Store Checkout ===")
print()

# Receive order information from the user

product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price ($): "))
quantity = int(input("Enter the quantity: "))
discount_percent = float(input("Enter the discount percentage (%): "))
shipping_cost = float(input("Enter the shipping cost ($): "))

print()

# Perform calculations
total_price = product_price * quantity
discount_amount = total_price * discount_percent / 100
final_price = total_price - discount_amount + shipping_cost

# Display the order summary
print("==== Order Summary ====")
print("Product:", product_name)
print("Product Price: $", product_price)
print("Quantity:", quantity)
print("Total Price: $", total_price)
print("Discount: $", discount_amount)
print("Shipping cost: $", shipping_cost)
print("Final Price: $", final_price)
