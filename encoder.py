def code_generator(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_text = ''
    for letter in text:
        if letter in alphabet: 
            letter_index = alphabet.index(letter) + 1
            if letter_index == len(alphabet):
                letter_index = 0
            encoded_text += alphabet[letter_index]
        else: 
            encoded_text += letter
    return encoded_text

text = input('Enter text: ')

encoded_text = code_generator(text)

print('Encoded message: ' + encoded_text)

