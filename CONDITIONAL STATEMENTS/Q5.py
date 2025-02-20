# 5. BMI Calculator
# Problem: Write a program that calculates the Body Mass Index (BMI) and
# categorizes the result:
# Below 18.5: Underweight
# 18.5 - 24.9: Normal weight
# 25 - 29.9: Overweight
# 30 and above: Obese

# Jainam Shah
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical score.")
else:
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
