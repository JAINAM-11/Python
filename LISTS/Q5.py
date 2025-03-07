# 5. Flatten a Nested List
# Problem: Write a function flatten_list(lst) that flattens a nested list (a list that contains
# other lists) into a single list.

# Jainam Shah
# Date: 06/03/25


def flatten_list(lst):
    flat_list = []

    for item in lst:
        if isinstance(item, list):  
            flat_list.extend(flatten_list(item))  
        else:
            flat_list.append(item) 

    return flat_list

nested_list = eval(input("Enter a nested list (e.g., [[1,2],[3,4,5],6,[7,[8,9]]]): "))

print("Flattened List:", flatten_list(nested_list))