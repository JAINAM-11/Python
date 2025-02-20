# 6. Vowel or Consonant
# Problem: Write a program that checks if a character is a vowel or a consonant.

# Jainam Shah

char = input("Enter a character: ")

if len(char) == 1:
    if char.isalpha():
        if char in "aeiouAEIOU":
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
    else:
        print("Invalid input! Please enter an alphabetic character.")
else:
    print("Invalid input! Please enter only 1 alphabetic character.")