"""
Exercise 03

Topic:
- Variables
- Data Types
- Input
- Output
- Operators 

Project:
Student Report

Objective:
Practice using variables, data types, user input,
operators, and output by creating a simple student report
that calculates and displays student information.
"""

# Get student information
student_id = input("Enter student ID: ")
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_class = input("Enter student class: ")

print()

# Get student grades
math_grade = float(input("Enter math grade: "))
science_grade = float(input("Enter science grade: "))
history_grade = float(input("Enter history grade: "))
english_grade = float(input("Enter english grade: "))
art_grade = float(input("Enter art grade: "))

print()

# Calculate results
total_grade = (
    math_grade + science_grade + history_grade
    + english_grade + art_grade
)              
average_grade = total_grade  / 5

# Display the student report
print("========== Student Report ==========")

print("Student ID: ", student_id)
print("Student Name: ", student_name)
print("Student Age: ", student_age)
print("Student Class: ", student_class)

print()

print("Math Grade: ", math_grade)
print("Science Grade: ", science_grade)
print("History Grade: ", history_grade)
print("English Grade: ", english_grade)
print("Art Grade: ", art_grade)

print()

print("Total Grade: ", total_grade)
print("Average Grade: ", average_grade)

print()
print("Report generated successfully.")
print("====================================")