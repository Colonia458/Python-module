# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.
price = float(input("Enter the item's price: "))
discount_percent = int(input("Enter the price discount: ")) / 100

def calculate_discount(price, discount_percent):
    discount = price * discount_percent
    bill = price - discount
    if discount_percent >= 0.2:
        print(f"Your bill is: {bill}")
    else:
        print(f"Your bill is: {price}.")
        print(f"Sorry, your discount was {discount_percent * 100}%, which was not above 20%")


calculate_discount(price, discount_percent)