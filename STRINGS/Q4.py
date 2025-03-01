# 4. Count Vowels and Consonants
# Problem: Write a function that counts the number of vowels and consonants in a
# given string. Consider that vowels are a, e, i, o, u (both lowercase and uppercase).

# Jainam Shah

def count_vowels_consonants(s):
    s=s.replace(" ","")
    for char in s:
        if char.isdigit() or not char.isalpha():
            return "Invalid input! Only alphabetic strings are allowed."
        
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return f"Vowels: {vowel_count}, Consonants: {consonant_count}"

user_input = input("Enter a string: ")
print(count_vowels_consonants(user_input))