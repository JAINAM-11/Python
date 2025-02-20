# 6. Palindrome Checker
# Problem: Write a program that checks if a given string is a palindrome. A string is a
# palindrome if it reads the same backward as forward.

# Jainam Shah

string = input("Enter a string: ")
is_palindrome = True
length = len(string)

for i in range(length // 2):
    if string[i] != string[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")