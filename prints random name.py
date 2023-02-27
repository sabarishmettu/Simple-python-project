#A program that takes a list of names as input and prints out a random name

import random

names = input("Enter a list of names separated by commas: ").split(',')
random_name = random.choice(names)
print("A random name from the list is:", random_name)
