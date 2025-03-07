# 4. Sum of Even and Odd Numbers
# Problem: Write a function sum_even_odd(lst) that returns the sum of all even numbers
# and the sum of all odd numbers in a list.

# Jainam Shah
# Date: 06/03/25


def sum_even_odd(lst):
    even_sum = 0
    odd_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

lst = input("Enter list elements separated by space: ").split()

for num in lst:
    lst = [int(num)]

even_sum, odd_sum = sum_even_odd(lst)

print("Sum of Even Numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)