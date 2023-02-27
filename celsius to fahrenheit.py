#A program that converts temperature between Celsius and Fahrenheit


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius or F for Fahrenheit): ")

if unit.upper() == "C":
    print("%.2f degree Celsius is equal to %.2f degree Fahrenheit" % (temp, celsius_to_fahrenheit(temp)))
elif unit.upper() == "F":
    print("%.2f degree Fahrenheit is equal to %.2f degree Celsius" % (temp, fahrenheit_to_celsius(temp)))
else:
    print("Invalid unit")
