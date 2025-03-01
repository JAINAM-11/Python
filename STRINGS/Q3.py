# 3. String Compression
# Problem: Write a function compress_string(s) that takes a string and returns a
# compressed version where repeated characters are replaced by the character
# followed by the count. For example, aaabbcc should be compressed to a3b2c2.

# Jainam Shah

def compress_string(s):
    if any(char.isdigit() for char in s) or not s.isalpha():
        return "Invalid input! Only alphabetic strings are allowed."
    
    compressed = ""
    count = 1 

    for i in range(1, len(s)):  
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count==1:
                compressed += s[i - 1]
            else:
                compressed += s[i - 1] + str(count) 
            count = 1

    compressed += s[-1] + str(count)

    return compressed

user_input = input("Enter a string: ")
print(compress_string(user_input))