"""
Exercise 02
Topic:
- Variables
- Data Types
- Input
- Output

Project:
Employee Card

Objective:
Practice using variables, different data types,
and user input by creating a simple employee profile.
"""

# Get employee information
employee_id = input("Enter employee ID: ")
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
job_title = input("Enter your job title: ")
department = input("Enter department: ")
company_name = input("Enter your company name: ")
salary = float(input("Enter your salary ($): "))
work_location = input("Enter work location: ")
email = input("Enter your email: ")
phone_number = input("Enter your phone number: ")

# Display the employee card
print("========== Employee Card ==========")
print("Employee ID: ", employee_id)
print("Full Name: ", full_name)
print("Age: ", age)
print("Job Title: ", job_title)
print("Department: ", department)
print("Company: ", company_name)
print("Salary: $", salary)
print("Work Location: ", work_location)
print("Email: ", email)
print("Phone Number: ", phone_number)
print("==================================")

print("Welcome to OpenAI!")
