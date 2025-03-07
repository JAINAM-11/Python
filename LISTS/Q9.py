# 9. Find the Index of an Element
# Problem: Write a function find_index(lst, element) that returns the index of the first
# occurrence of a given element in a list. If the element is not found, return -1.

# Jainam Shah
# Date: 06/03/25


def find_index(lst, element):
    for i in range(len(lst)): 
        if lst[i] == element:
            return i
    return -1

user_input = input("Enter elements of the list separated by spaces: ")
lst = []

for num in user_input.split():
    lst.append(int(num)) 

element = int(input("Enter the element to find: "))

print("Index of element:", find_index(lst, element))