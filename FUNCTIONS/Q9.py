# 9. GCD (Greatest Common Divisor)
# Problem: Write a function gcd(a, b) that computes the greatest common divisor of two
# integers a and b using the Euclidean algorithm.
# Input: Two integers a and b
# Output: The greatest common divisor of a and b

# Jainam Shah


def input_number(n):
    while True:
        try:
            value = float(input(f"Enter Number {n} : "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")


def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


number1 = input_number(1)
number2 = input_number(2)
result = gcd_subtraction(number1, number2)
print(f"The GCD of {number1} and {number2} is: {result}")