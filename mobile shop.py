class MobileShop:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        if len(self.devices) < 10:
            self.devices.append(device)
            print("Device added successfully!")
        else:
            print("Sorry, the shop is full and cannot accept more devices.")

    def remove_device(self, device):
        if device in self.devices:
            self.devices.remove(device)
            print("Device removed successfully!")
        else:
            print("Sorry, the device is not in the shop.")

    def list_devices(self):
        if len(self.devices) == 0:
            print("The shop is currently empty.")
        else:
            print("The devices in the shop are:")
            for device in self.devices:
                print("- " + device)

# Example usage:
shop = MobileShop()

while True:
    print("What device would you like to buy? (type 'exit' to quit)")
    device_name = input()

    if device_name.lower() == 'exit':
        break

    if device_name in shop.devices:
        shop.remove_device(device_name)
    else:
        print("Sorry, that device is not available for purchase.")
    
    print("Thank you for your purchase!")
    shop.list_devices()
