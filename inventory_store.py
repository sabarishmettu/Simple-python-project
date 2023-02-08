# Program to manage store inventory

# define a class to store inventory data
class Inventory:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

# define a function to add items to the inventory
def add_item(inventory, item, quantity):
    inventory[item] = quantity
    return inventory

# define a function to remove items from the inventory
def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

# define a function to edit the quantity of items in the inventory
def edit_item(inventory, item, quantity):
    if item in inventory:
        inventory[item] = quantity
    return inventory

# define a function to view the inventory
def view_inventory(inventory):
    for item in inventory:
        print(f"Item: {item}, Quantity: {inventory[item]}")

# define a function to save the inventory to a file
def save_inventory(inventory, file_name):
    with open(file_name, 'w') as file:
        for item in inventory:
            file.write(f"{item},{inventory[item]}\n")

# define a function to read the inventory from a file
def read_inventory(file_name):
    inventory = {}
    with open(file_name, 'r') as file:
        for line in file:
            item, quantity = line.strip().split(',')
            inventory[item] = int(quantity)
    return inventory

# main program
inventory = {}

while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Edit Item")
    print("4. View Inventory")
    print("5. Save Inventory")
    print("6. Read Inventory")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        inventory = add_item(inventory, item, quantity)
    elif choice == '2':
        item = input("Enter item: ")
        inventory = remove_item(inventory, item)
    elif choice == '3':
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        inventory = edit_item(inventory, item, quantity)
    elif choice == '4':
        view_inventory(inventory)
    elif choice == '5':
        file_name = input("Enter file name: ")
        save_inventory(inventory, file_name)
    elif choice == '6':
        file_name = input("Enter file name: ")
        inventory = read_inventory(file_name)
    elif choice == '7':
        break
    else:
        print("Invalid choice!")