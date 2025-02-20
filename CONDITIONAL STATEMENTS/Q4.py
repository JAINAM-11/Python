# 4. Even or Odd Number
# Problem: Write a program that checks whether a given integer is even or odd.

# Jainam Shah

try:
    num = int(input("Enter an Integer: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical score.")
else:
    if num==0:
        print(f"{num} is neither Even nor Odd.")
    elif num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")