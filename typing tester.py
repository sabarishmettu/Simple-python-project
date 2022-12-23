import tkinter
import time
import random

#Function to extract ingredients from a list
def get_ingredients():
    #Open a file and read the lines
    file = open('Typing.txt', 'r')
    lines = file.readlines()
    file.close()

    #Initialize a list to store ingredients
    ingredients = []

    #Loop through each line
    for line in lines:
        #Get the ingredient by cutting off everything before the comma
        ingredient = line[line.find(',') + 1:]

        #Get rid of the excess spaces and add to the list
        ingredient = ingredient.replace('\n', '')
        ingredient = ingredient.strip()
        ingredients.append(ingredient)

    #Return the list of ingredients
    return ingredients

#Function to generate random ingredient and set text
def get_random_ingredient(event=None):
    #Get the list of ingredients
    ingredients = get_ingredients()

    #Get a random index within the ingredients list
    idx = random.randrange(0, len(ingredients))

    #Get the ingredient and set the text
    ingredient = ingredients[idx]
    input_var.set(ingredient)

#Function to get the typed text, check spelling, and return result
def check_spelling(event=None):
    #Get the text from the input
    text = input_var.get()

    #If the text matches the ingredient then correct
    if text == ingredient:
        result = 'Correct'
    #If the text does not match the ingredient then incorrect
    else:
        result = 'Incorrect'

    #Set the result into the output
    output_var.set(result)

#Function to get the typed text and calculate the words per minute
def get_wpm(event=None):
    #Get the text from the input
    text = input_var.get()

    #If the text matches the ingredient then set the start time
    if text == ingredient:
        #Set the current time to the start time
        start_time = time.time()

        #Clear the time variable
        time_var.set('')

        #Clear the text variable
        input_var.set('')

        #Getynchronize the input with the output
        output_var.set('')

        #Generate another ingredient
        get_random_ingredient()
    #If the text does not match the ingredient then calculate and display the WPM
    else:
        #Calculate the elapsed time
        elapsed_time = time.time() - start_time

        #Calculate the words per minute
        wpm = len(text.split()) / elapsed_time * 60

        #Set the time output to the WPM
        time_var.set(str(int(wpm)))

#Function to quit the application
def quit():
    root.quit()

# Main function
def main():
    #Create the window
    root = tkinter.Tk()
    root.configure(padx=10, pady=10, bg='#228b22',bd=5,width=600)

    #Create an empty string to store the ingredient
    global ingredient

    #Create a list of ingredients
    ingredients = get_ingredients()

    #Get a random index within the ingredients list
    idx = random.randrange(0, len(ingredients))

    #Get the ingredient
    ingredient = ingredients[idx]

    #Create variables for the input and output
    global input_var
    global output_var
    global time_var
    input_var = tkinter.StringVar()
    output_var = tkinter.StringVar()
    time_var = tkinter.StringVar()

    #Create the input and output objects
    top_frame = tkinter.Frame(root)
    top_frame.pack()
    bottom_frame = tkinter.Frame(root)
    bottom_frame.pack()
    input_obj = tkinter.Entry(top_frame, textvariable=input_var, bg='#32ff32',bd=5)
    output_obj = tkinter.Label(top_frame, textvariable=output_var, bg='#32ff32',bd=5)
    time_obj = tkinter.Label(top_frame, textvariable=time_var, bg='#32ff32',bd=5)

    #Create a quit button
    quit_button = tkinter.Button(bottom_frame, text='Quit',bg='#32ff32',bd=5, command=quit)

    #Create the textfield to display the ingredient
    ingredient_obj = tkinter.Label(bottom_frame, text='Ingredient: ' + ingredient, bg='#32ff32',bd=5)

    #Add the objects to the window and bind them to functions
    ingredient_obj.pack()
    input_obj.pack()
    output_obj.pack()
    time_obj.pack()
    quit_button.pack(side='right')
    ingredient_obj.bind('<Button-1>', get_random_ingredient)
    input_obj.bind('<Key>', get_wpm)
    input_obj.bind('<Key-Return>', check_spelling)

    #Enter the main loop
    root.mainloop()

#Call the main function
main()
