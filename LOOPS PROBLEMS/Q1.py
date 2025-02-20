# 1. Sum of Natural Numbers
# Problem: Write a program that calculates the sum of all natural numbers up to a
# given number n using a loop. The sum of the first n natural numbers is given by the
# formula:Sum=1+2+3+⋯+n\ text{Sum} = 1 + 2 + 3 + \dots + nSum=1+2+3+⋯+n

# Jainam Shah

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    sum = 0
    for i in range(1, number + 1):
        sum += i
    print("Sum of first", number, "natural numbers is:", sum)