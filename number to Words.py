# Dictionary to store the mapping of digit to word
digit_to_word = {
    0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 
    7: 'Seven', 8: 'Eight', 9: 'Nine'
}

# Dictionary to store the mapping of two-digit numbers to word
two_digit_to_word = {
    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 
    70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
}

# List to store the mapping of position to word
position_to_word = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion']

# Check if the number is zero
if number == 0:
    return digit_to_word[0]

# Convert the number to a list of digits
digits = [int(d) for d in str(number)]

# Reverse the list of digits for easier processing
digits.reverse()

# Initialize an empty string to store the words
words = ''

# Process the digits in groups of three
for i in range(0, len(digits), 3):
    
    # Get the current group of three digits
    group = digits[i:i+3]
    
    # Get the position of the current group
    position = i // 3
    
    # Initialize an empty string to store the words for the current group
    group_words = ''
    
    # Process the digits in the current group
    for j in range(len(group)):
        
        # Get the digit at the current position
        digit = group[j]
        
        # Get the word for the digit at the current position
        if j == 0:
            digit_word = digit_to_word[digit]
        elif j == 1 and digit == 1:
            # Handle two-digit numbers from 10 to 19
            digit_word = two_digit_to_word[digit*10 + group[j-1]]
        elif j == 1 and digit != 0:
            # Handle two-digit numbers from 20 to 99
            digit_word = two_digit_to_word[digit*10]
        else:
            digit_word = ''
            
        # Add the word for the current digit to the words for the current group
        group_words = digit_word + ' ' + group_words
    
    # Add the word for the position to the words for the current group
    if group_words != '':
        group_words += ' ' + position_to_word[position]
    
    # Add the words for the current group to the overall words
    words = group_words + ' ' + words

# Remove any extra spaces and return the words
return words.strip()
