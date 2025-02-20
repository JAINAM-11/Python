# 7. Prime Number Generator
# Problem: Write a function generate_primes(n) that generates a list of prime numbers up
# to n. A prime number is a number greater than 1 that has no divisors other than 1
# and itself.
# Input: Integer n
# Output: List of prime numbers up to n

# Jainam Shah

def input_number():
    while True:
        try:
            value = int(input(f"Enter Number : "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")



n = input_number()
print("Prime Numbers : ", end=" ")
primes = generate_primes(n)
