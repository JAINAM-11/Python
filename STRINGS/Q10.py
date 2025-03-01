# 10. String Rotation
# Problem: Write a function is_rotation(s1, s2) that checks if one string is a rotation of
# another string. For example, "abc" is a rotation of "cab", but "abc" is not a rotation of
# "acb".

# Jainam Shah

def is_rotation(s1, s2):
    
    if len(s1) != len(s2):
        return "No, the strings are not rotations (different lengths)."
    
    if s2 in (s1 + s1):
        return "Yes, the strings are rotations."
    else:
        return "No, the strings are not rotations."

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print(is_rotation(str1, str2))
