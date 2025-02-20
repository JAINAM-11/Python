# 10. Pattern Printing
# Problem: Write a program that prints a pattern of numbers in the following format
# (for n = 5):
# Copy
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Jainam Shah

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()