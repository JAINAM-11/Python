# 3. Multiplication Table
# Problem: Write a program that prints the multiplication table of a given number n
# from 1 to 10.

# Jainam Shah

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)
