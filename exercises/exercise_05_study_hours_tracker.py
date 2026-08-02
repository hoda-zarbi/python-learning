"""
Exercise 05

Topic:
- Variables
- Data Types
- Input
- Output
- Loops

Project:
Study Hours Tracker

Objective:
Practice using variables, data types, user input,
output and loops by creating a simple study hours
tracker program.
"""

print("===== Study Hours Tracker =====")
print()

number_of_days = int(input("How many days do you want to track? "))

for day in range(1, number_of_days + 1):
    study_hours = float(input("Enter study hours: "))
    print("Day", day, "Study Hours:", study_hours)

print()
print("==============================")
print("Good luck with your studies!")
