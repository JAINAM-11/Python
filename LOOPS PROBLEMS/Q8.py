# 8. Multiplication of Elements in List
# Problem: Write a program that multiplies all the elements of a given list of numbers
# and prints the result. Use a loop to multiply each element.

# Jainam Shah

numbers = [2, 3, 4, 5]
product = 1
i = 0
while i < len(numbers):
    product *= numbers[i]
    i += 1
print("Product:", product)