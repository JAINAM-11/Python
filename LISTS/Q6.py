# 6. Find Common Elements in Two Lists
# Problem: Write a function common_elements(list1, list2) that returns a list of common
# elements between two lists. The order of the elements in the result should follow the
# order in list1.

# NAME: JAINAM SHAH
# DATE: 06/03/25

def common_elements(list1, list2):
    result = []
    for item in list1:
        try:
            list2.index(item)
            result.append(item)
        except ValueError:
            pass  
    return result

list1 = input("Enter the numbers in list1 with space: ").split()
list2 = input("Enter the numbers in list2 with space: ").split()

list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

print(common_elements(list1, list2))    