# 5. Fibonacci Series
# Problem: Write a program that prints the first n numbers in the Fibonacci sequence
# using a loop. The Fibonacci sequence starts with 0, 1, and each subsequent number
# is the sum of the previous two.

# Jainam Shah

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    a, b = 0, 1
    print("Fibonacci series:", a, b, end=" ")

    for _ in range(number - 2):
        c = a + b
        print(c, end=" ")
        a, b = b, c
        
    print()