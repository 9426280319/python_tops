# Create a mini-project where students combine conditional statements, loops, and functions to create a basic Python application, such as a simple calculator or a grade management system.

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

# Main program
students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    grade = calculate_grade(marks)
    students[name] = {"marks": marks, "grade": grade}

print("\nStudent Grades:")
for name, info in students.items():
    print(f"{name}: Marks = {info['marks']}, Grade = {info['grade']}")
