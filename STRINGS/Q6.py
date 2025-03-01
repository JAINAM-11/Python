# 6. Longest Substring Without Repeating Characters
# Problem: Write a function longest_substring(s) that returns the length of the longest
# substring in a string s without repeating characters.

# Jainam Shah

def longest_substring(s):
    words=s.split()
    max_length=0
    length=0
    for word in words:
        distinct_chars = []
        for char in word:
            if char not in distinct_chars:
                distinct_chars.append(char)
                length+=1
        if length>max_length:
            max_length=length
            length=0
    

    return max_length

user_input = input("Enter a string: ")
result = longest_substring(user_input)

print("Length of the longest substring without repeating characters:", result)