# 3. Leap Year Checker
# Problem: Write a program that checks if a given year is a leap year. A year is a leap
# year if:
# It is divisible by 4,
# If divisible by 100, it must also be divisible by 400.

# Jainam Shah
try:
    year = int(input("Enter a Year: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    if(1000<= year <=9999):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print("Invalid Input")