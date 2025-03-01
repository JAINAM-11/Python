# 2. Anagram Checker
# Problem: Write a function are_anagrams(s1, s2) that checks if two given strings are
# anagrams of each other. Two strings are anagrams if they contain the same
# characters with the same frequencies, but possibly in different orders.

# Jainam Shah

def are_anagrams(s1, s2):
    s1, s2 = s1.replace(" ", "").lower(), s2.replace(" ", "").lower()
    flag=False
    if len(s1)!=len(s2):
        flag=False
    for char in s1:
        if char in s2:
            flag=True
        else:
            flag=False
            break
    if flag:
        return "String are anagrams"
    else:
        return "String are not anagrams"


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print(are_anagrams(str1, str2))