# 9. Count Vowels in a StringProblem: Write a program that 
# counts how many vowels are present in a given string. 
# Consider vowels as a, e, i, o, u (both uppercase and lowercase).

# Jainam Shah

string = input("Enter a string: ")
vowel_count = 0
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the string : ", vowel_count)