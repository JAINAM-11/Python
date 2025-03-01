# 5. Palindrome Check
# Problem: Write a function is_palindrome(s) that checks if a string is a palindrome. A
# string is a palindrome if it reads the same backward as forward, ignoring spaces,
# punctuation, and case.

# Jainam Shah

import string

def is_palindrome(s):
    return "Yes, it's a palindrome." if s == s[::-1] else "No, it's not a palindrome."

user_input = input("Enter a string: ")
print(is_palindrome(user_input))
