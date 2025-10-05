# Today's lucky score calculator

# Using Random Functions
from random import *

# Name
name = "hajin" #Please write your name between."

# Generating random scores between 1 and 100
luck_score = randint(1, 100)

# Set the message according to the score
if luck_score >= 80:
    message = "lucky today! 🍀"
elif luck_score >= 50:
    message = "It's a decent day 🙂"
else:
    message = "It's a bad day 😢"

# Result
print("\n=== Today's lucky score ===")
print(name + "'s luck score is " + str(luck_score) + " point!")
print(message)



