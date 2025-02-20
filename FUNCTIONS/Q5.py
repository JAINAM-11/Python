# 5. Find Maximum in List
# Problem: Write a function find_max(numbers) that takes a list of numbers and returns
# the largest number in the list without using built-in functions like max().
# Input: List of numbers
# Output: The largest number in the list

# Jainam Shah

def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    
    return max_value

try:
    input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    result = find_max(input_list)
    print(f"The maximum value in the list is: {result}")
except ValueError:
    print("Invalid input! Please enter only numbers separated by spaces.")