# 9. Remove Punctuation
# Problem: Write a function remove_punctuation(s) that removes all punctuation
# characters (e.g., ., ,, !, ?) from a given string.

# Jainam Shah

import string

def remove_punctuation(s):
    result=""
    punctuation=",.!?"
    for char in s:
        if char in punctuation:
            continue
        else:
            result=result+char
    return result

user_input = input("Enter a string: ")
print("String without punctuation:", remove_punctuation(user_input))
