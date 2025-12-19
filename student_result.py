# Student Result Management System

name = input("Enter student name: ")
roll = input("Enter roll number: ")

marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
