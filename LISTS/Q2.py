# 2. Find the Second Largest Element
# Problem: Write a function second_largest(nums) that finds the second largest element
# in a list of integers. If the list has less than two distinct elements, return None.

# Jainam Shah
# Date: 06/03/25

def second_largest(nums):
    if len(nums) < 2:
        return None

    largest = second = None

    for num in nums:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second

nums = input("Enter list elements separated by space: ").split()

for num in nums:
    nums = [int(num)]

result = second_largest(nums)
print("Second Largest Element:", result if result is not None else "None")