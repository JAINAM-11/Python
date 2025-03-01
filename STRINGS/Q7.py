# 7. Find All Substrings
# Problem: Write a function find_substrings(s) that returns a list of all possible substrings
# of a given string s.

# Jainam Shah

def find_substrings(s):
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(s[i:j])

    return substrings

user_input = input("Enter a string: ")
result = find_substrings(user_input)
print(result)