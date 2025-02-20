# 1. Student Grading System
# Problem: Write a program that takes a student's score as input and prints the grade
# based on the following criteria:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60

# Jainam Shah

try:
    score = float(input("Enter The Student's Score : "))
except ValueError:
    print("Invalid input! Please enter a valid numerical score.")
else:
    if score >= 90:
        print("A")
    if score >= 80 and score < 90:
        print("B")
    if score >= 70 and score < 80:
        print("C")
    if score >= 60 and score < 70:
        print("D")
    if score < 60:
        print("F")
