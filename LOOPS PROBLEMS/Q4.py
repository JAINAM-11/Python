# 4. Prime Number Checker
# Problem: Write a program that checks if a given number n is prime. A prime number
# is a number greater than 1 and divisible only by 1 and itself.

# Jainam Shah

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    if number > 1:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")
    else:
        print(number, "is not a prime number.")