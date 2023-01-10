# Program for an ice cream shop

# Initializing the menu
ice_cream_menu = {
    "Vanilla": 10,
    "Chocolate": 15,
    "Strawberry": 20,
    "Mango": 25
}

# Ask user to select an ice cream
ice_cream = input("Please select an ice cream: ")

# Get the price of the selected ice cream
price = ice_cream_menu.get(ice_cream)

# Print the selected ice cream and its price
print("You have selected " + ice_cream + " ice cream and its price is " + str(price) + " rupees.")
