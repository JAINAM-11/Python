# 10. Age Group Classification
# Problem: Write a program that classifies a person based on their age:
# 0-12: Child
# 13-19: Teenager
# 20-64: Adult
# 65 and above: Senior

# Jainam Shah

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    if age < 0:
        print("Invalid age!")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")