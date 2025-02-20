# 6. Sum of Digits Function
# Problem: Write a function sum_of_digits(n) that calculates and returns the sum of the
# digits of a given integer n. You can extract each digit of n using a loop.
# Input: Integer n
# Output: The sum of the digits of n

# Jainam Shah


def input_number():
    while True:
        try:
            value = int(input(f"Enter Number : "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total

number=input_number()
print(f"The Sum of Digits of {number} is : {sum_of_digits(number)}")