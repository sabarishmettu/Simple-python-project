#This code converts Roman numbers to decimals

#Defining a dictionary for Roman numerals
roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

#Function to convert Roman numerals to decimals
def convert_roman_to_decimal(input):
    decimal = 0
    for i in range(len(input)):
        if i > 0 and roman_numerals[input[i]] > roman_numerals[input[i - 1]]:
            decimal += roman_numerals[input[i]] - 2 * roman_numerals[input[i - 1]]
        else:
            decimal += roman_numerals[input[i]]
    return decimal

#Taking input from the user
input = input("Enter the Roman number: ")

#Function call
result = convert_roman_to_decimal(input)

#Displaying the result
print("The decimal equivalent of ", input, "is", result)