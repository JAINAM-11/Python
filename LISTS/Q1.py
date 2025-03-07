# 1. Merge Two Lists
# Write a function merge_lists(list1, list2) that merges two sorted lists into a
# single sorted list. Do not use the built-in sort() method.

# NAME: JAINAM SHAH
# DATE: 06/03/25

def merge_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

list1 = input("Enter sorted list1 elements separated by space: ").split()
list2 = input("Enter sorted list2 elements separated by space: ").split()


list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

print("Merged Sorted List:", merge_lists(list1, list2))