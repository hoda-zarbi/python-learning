"""
Exercise 02
Topic: variables, Data Types, Input()

Project:
Employee Card

Objective:
Practice using variables, different data types,
and user input by creating a simple employee profile.
"""

# Get employee information
full_name = input("Enter your full name: ")
age = int(input("Enter your age: ")
gender = input("Enter your gender: ")
job_title = input("Enter your job title: ")
salary = float(input("Enter your salary ($): "))
company_name = input("Enter your company name: ")
nationality = input("Enter your nationality: ")
email = input("Enter your email: ")
phone_number = input("Enter your phone number: ")

# Display the employee card
print("\n========== Employee Card ==========")
print("Full Name:", full_name)
print("Age:", age)
print("Gender:", gender)
print("Job Title:", job_title)
print("Salary: $", salary)
print("Company Name:", company_name)
print("Nationality:", nationality)
print("Email:", email)
print("Phone Number:", phone_number)
print("===================================")
