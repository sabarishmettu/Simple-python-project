# Stationery Shop inventory
items = {
    "pen": {"quantity":10, "price": 2.0},
    "pencil": {"quantity":12, "price":1.5},
    "eraser": {"quantity":5, "price":0.5},
    "ruler": {"quantity":7, "price":1.2},
    "notebook": {"quantity":20, "price":3.5},
    "folder": {"quantity":15, "price":2.0},
    "stapler": {"quantity":8, "price":3.5},
    "scissors": {"quantity":10, "price":4.0},
    "tape": {"quantity":6, "price":1.5},
    "glue": {"quantity":4, "price":2.0}
}

# Print all items and their quantities
for item, details in items.items():
    print(f"{item} - Quantity: {details['quantity']} Price: {details['price']}")

# Allow user to select an item
item_name = input("Enter the name of the item you want to purchase: ")
item_quantity = int(input("Enter the Quantity of the item you want to purchase: "))

# Check if item is in inventory
if item_name in items:
    if item_quantity <= items[item_name]['quantity']:
        item_price = item_quantity * items[item_name]['price']
        print(f"The cost of {item_quantity} {item_name} is {item_price}")
        print("Thank you for buying!")
    else:
        print(f"We have only {items[item_name]['quantity']} {item_name} in stock")
else:
    print(f"Item {item_name} is not available in our inventory")
    print("Thank you for buying!")
