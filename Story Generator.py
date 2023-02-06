import random

# Lists of story components 
characters = ["farmer", "princess", "dragon", "wizard", "knight"]
adjectives = ["angry", "happy", "sad", "eager", "lazy"]
places = ["castle", "forest", "cave", "mountain", "village"]
actions = ["ran", "jumped", "cried", "danced", "slept"]

# Generate random story
print("Once upon a time, there was a " + random.choice(characters) + " who was feeling " + random.choice(adjectives) + ". They decided to go to the " + random.choice(places) + " and " + random.choice(actions) + ".")