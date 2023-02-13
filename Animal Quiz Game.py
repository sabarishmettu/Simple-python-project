# Animal Quiz Game

# Declare the variables
score = 0

# Ask the user to enter their name
name = input("Please enter your name: ")

# Welcome the user
print("Welcome to the Animal Quiz Game, " + name + "!")

# Ask the user a question
print("What is the scientific name for a lion?")

# Give the user three chances to answer the question
for i in range(3):
    answer = input("Answer: ")
    # Check if the answer is correct
    if answer == "Panthera leo":
        # Increment score by 1
        score += 1
        print("Correct!")
        break
    else:
        print("Incorrect. Please try again.")

# Ask the user another question
print("What is the scientific name for a chimpanzee?")

# Give the user three chances to answer the question
for i in range(3):
    answer = input("Answer: ")
    # Check if the answer is correct
    if answer == "Pan troglodytes":
        # Increment score by 1
        score += 1
        print("Correct!")
        break
    else:
        print("Incorrect. Please try again.")

# Ask the user another question
print("What is the scientific name for a gorilla?")

# Give the user three chances to answer the question
for i in range(3):
    answer = input("Answer: ")
    # Check if the answer is correct
    if answer == "Gorilla gorilla":
        # Increment score by 1
        score += 1
        print("Correct!")
        break
    else:
        print("Incorrect. Please try again.")

# Show the user the final score
print("Your final score is " + str(score) + "/3.")