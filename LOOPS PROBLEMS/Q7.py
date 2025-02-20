# 7. Sum of Digits
# Problem: Write a program that calculates the sum of the digits of a given number n.
# Use a loop to extract each digit and add it to a sum.

# Jainam Shah

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number //= 10
    print("Sum of digits is:", sum_of_digits)