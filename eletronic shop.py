class ElectronicShop:
    def __init__(self):
        self.devices = []
        self.total_sales = 0

    def add_device(self, device):
        self.devices.append(device)

    def sell_device(self, device_id):
        for device in self.devices:
            if device.id == device_id:
                self.total_sales += device.price
                self.devices.remove(device)
                return True
        return False

class Device:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# Create an instance of the ElectronicShop class
shop = ElectronicShop()

# Get input from the user for each device
for i in range(20):
    id = int(input(f"Enter ID for device {i+1}: "))
    name = input(f"Enter name for device {i+1}: ")
    price = float(input(f"Enter price for device {i+1}: "))
    device = Device(id, name, price)
    shop.add_device(device)

# Get input from the user for the device ID to sell
device_id = int(input("Enter the ID of the device you want to sell: "))
if shop.sell_device(device_id):
    print("Device sold!")
else:
    print("Device not found.")

# Print the remaining devices and total sales
print("Remaining devices:")
for device in shop.devices:
    print(device.name)
print("Total sales: $", shop.total_sales)
