# 1. String Reversal
# Problem: Write a function that reverses a given string without using Python’s built-in
# reverse methods (e.g., reversed(), slicing). Implement the reversal manually using a
# loop.

# Jainam Shah

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    
    return reversed_str

user_input = input("Enter a string: ")
print(reverse_string(user_input))
