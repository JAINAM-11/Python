# 8. Rotate List
# Problem: Write a function rotate_list(lst, k) that rotates a list lst to the right by k
# positions. If k is greater than the length of the list, rotate it by k % len(lst) positions.

# NAME: JAINAM SHAH
# DATE: 06/03/25

def rotate_list(lst, k):
    if not lst:  
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

user_input = input("Enter elements of the list separated by spaces: ")
lst = []  

for num in user_input.split(): 
    lst.append(int(num)) 

k = int(input("Enter the number of positions to rotate: "))

print("Rotated List:", rotate_list(lst, k))
