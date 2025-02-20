# 4. Palindrome Function
# Problem: Write a function is_palindrome(string) that checks if a given string is a
# palindrome. A palindrome is a word or phrase that reads the same forwards and
# backwards, ignoring spaces, punctuation, and capitalization.
# Input: A string
# Output: Boolean (True or False)

# Jainam Shah

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a string: ")
print(is_palindrome(input_string))