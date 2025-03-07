# 10. List Comprehension Filter
# Problem: Write a function filter_multiples_of_n(lst, n) that uses list comprehension to
# return a new list containing only the numbers in lst that are divisible by n.

# NAME: JAINAM SHAH
# DATE: 06/03/25

def filter_multiples_of_n(lst, n):
    divisable=[]
    for item in lst: 
        if item % n == 0:
            divisable.append(item)
    return divisable 

user_input = input("Enter elements of the list separated by spaces: ")
lst = []

for num in user_input.split():
    lst.append(int(num))

n = int(input("Enter the number to filter multiples of: "))

print("Filtered List:", filter_multiples_of_n(lst, n))