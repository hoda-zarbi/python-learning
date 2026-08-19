"""
Topic: Functions
Example: Student Grade Calculator

This file demonstrates how a function
can perform a reusable calculation in Python.
"""

print("===== Student Grade Calculator =====")
print("Calculating student average...")

math_grade = float(input("Enter math grade: "))
python_grade = float(input("Enter Python grade: "))
english_grade = float(input("Enter English grade: "))

def calculate_average(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3
    return average
print()

average_grade = calculate_average(
    math_grade,
    python_grade,
    english_grade
)

print("Average grade:", average_grade)
print("✅ Calculation completed!")
