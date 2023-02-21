
def code_generator(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_text = ''
    decoded_text = ''
    for letter in text:
        if letter in alphabet: 
            letter_index = alphabet.index(letter) + 1
            if letter_index == len(alphabet):
                letter_index = 0
            encoded_text += alphabet[letter_index]
            decoded_text += alphabet[letter_index-1] 
        else: 
            encoded_text += letter
            decoded_text += letter
    return encoded_text, decoded_text

text = input('Enter text: ')

encoded_text, decoded_text = code_generator(text)

print('Encoded message: ' + encoded_text)
print('Decoded message: ' + decoded_text)
