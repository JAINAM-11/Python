# 7. Find the Missing Number
# Problem: Write a function find_missing_number(lst) that takes a list of integers from 1 to
# n with one missing number. The list contains unique integers but is missing one
# number.

# NAME: JAINAM SHAH
# DATE: 06/03/25

def find_missing_number(lst):
    missing=[]
    n = len(lst) + 1  
    for num in range(1, n + 1):  
        if lst.count(num) == 0:  
            missing.append(num)
    return missing

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Missing number:", find_missing_number(lst))