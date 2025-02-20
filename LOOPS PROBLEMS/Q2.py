# 2. Factorial Calculation
# Problem: Write a program that calculates the factorial of a number n using a loop.
# The factorial of n (denoted as n!) is the product of all positive integers less than or
# equal to n.

# Jainam Shah

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is:", factorial)