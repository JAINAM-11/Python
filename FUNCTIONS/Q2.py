# 2. Temperature Conversion
# Problem: Write a program with functions to convert temperatures between Celsius
# and Fahrenheit. Create two functions:
#  celsius_to_fahrenheit(celsius) to convert Celsius to Fahrenheit
#  fahrenheit_to_celsius(fahrenheit) to convert Fahrenheit to Celsius
# Input: Temperature (Celsius or Fahrenheit)
# Output: The converted temperature

# Jainam Shah

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def input_temprature(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

celsius = input_temprature("Enter temperature in Celcius: ")
fahrenheit = input_temprature("Enter temperature in Fahrenheit: ")

print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius): }°F")
print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit): }°C")