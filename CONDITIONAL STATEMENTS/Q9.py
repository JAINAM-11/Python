# 9. Discount Calculator
# Problem: Write a program that calculates the discount based on the price:
# Price < 50: No discount
# Price >= 50 and < 100: 10% discount
# Price >= 100 and < 200: 20% discount
# Price >= 200: 30% discount

# Jainam Shah

try:
    price = float(input("Enter the price: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    if price < 50:
        discount = 0
    elif price < 100:
        discount = 10
    elif price < 200:
        discount = 20
    else:
        discount = 30

    discounted_price = price - (price * discount / 100)
    print(f"Discount: {discount}%, Final Price: {discounted_price:.2f}")