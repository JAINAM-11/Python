# 3. Remove Duplicates from List
# Problem: Write a function remove_duplicates(lst) that removes duplicate elements from
# a list while maintaining the order of the original elements.

# Jainam Shah
# Date: 06/03/25

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

lst = input("Enter list elements separated by space: ").split()

for num in lst:
    lst = [int(num)]

print("List after removing duplicates:", remove_duplicates(lst))