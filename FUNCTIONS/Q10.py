# 10. Shopping Cart Total
# Problem: Write a function calculate_total(cart) that calculates the total price of items in
# a shopping cart. The cart will be represented as a list of tuples where each tuple
# contains the item price and the quantity purchased. Your function should return the
# total price.
# Input: List of tuples cart = [(price1, quantity1), (price2, quantity2), ...]
# Output: The total price of the items in the cart

# Jainam Shah

def calculate_total(cart):
    total_price = 0
    for price, quantity in cart:
        total_price += price * quantity
    return total_price

def input_cart():
    cart = []
    while True:
        try:
            price = float(input("Enter the price of the item: "))
            quantity = int(input("Enter the quantity of the item: "))
            cart.append((price, quantity))

            another_item = input("Do you want to add another item? (y/n): ").lower()
            if another_item != 'y':
                break
        except ValueError:
            print("Invalid input! Please enter valid numbers for price and quantity.")
    
    return cart

cart = input_cart()
total = calculate_total(cart)
print(f"The total price of the items in the cart is: {total:.2f}")
