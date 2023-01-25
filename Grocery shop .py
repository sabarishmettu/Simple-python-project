# Define a dictionary to store the item names and prices
items = {
    "apple": 25,
    "banana": 15,
    "orange": 30,
    "lemon": 10,
    "lime": 10,
    "grapes": 50,
    "watermelon": 10,
    "strawberries": 75,
    "blueberries": 10,
    "blackberries": 10,
    "peach": 40,
    "plum": 40,
    "pear": 50,
    "mango": 10,
    "kiwi": 50,
    "pineapple": 20,
    "papaya": 150,
    "coconut": 25,
    "avocado": 10,
    "guava": 15
}

# Define a function to check out the items in the cart
def checkout(cart):
    total_price = 0
    for item in cart:
        total_price += items[item]
    return total_price

# Initialize an empty cart
cart = []

# Continuously prompt the user to add items to the cart
while True:
    item = input("Enter the name of an item to add to the cart (or 'checkout' to finish): ").lower()
    if item == "checkout":
        break
    elif item in items:
        cart.append(item)
    else:
        print("Invalid item. Please enter a valid item name.")

# Print the total cost of the items in the cart
print("Total cost: ${:.2f}".format(checkout(cart)))
