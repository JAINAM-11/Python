# 7. Password Validator
# Problem: Write a program that checks if a given password meets the following
# criteria:
# At least 8 characters long
# Contains at least one uppercase letter
# Contains at least one digit
# Contains at least one special character (e.g., @, #, $, etc.)

# Jainam Shah

password = input("Enter your password: ")

has_upper = False
has_digit = False
has_special = False
special_chars = "!@#$%^&*(),.?\":{}|<>"

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True
    
    if has_upper and has_digit and has_special:
        print("Password is strong.")
    else:
        print("Password does not meet the criteria.")
else:
    print("Password does not meet the criteria.")