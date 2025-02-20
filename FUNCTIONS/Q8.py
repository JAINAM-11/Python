# 8. Fibonacci Sequence
# Problem: Write a function fibonacci(n) that returns the first n Fibonacci numbers. The
# Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, 8, 13, ....
# Input: Integer n
# Output: List of the first n Fibonacci numbers

# Jainam Shah
def input_number():
    while True:
        try:
            value = int(input(f"Enter Number : "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = input_number()
print("Fibonacci Numbers : ", end=" ")
fibonacci(n)
