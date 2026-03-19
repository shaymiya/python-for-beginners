# DICE ROLLING GAME
# 1- ask the user if they want to roll the dice: Roll the dice? (y/n)
# 2- check if the user input is valid (y or n), if not print Invalid choice!
# 3- if y, roll 2 dice 1-6, formatting (dice1, dice2)
# 4- if n, end the program and print Thanks for playing!

# import the random module for random number
import random

user_input = "" # store the user input

# make a simple function for rolling the dice
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"({dice1}, {dice2})")

# use infinite while loop for the game core loop
while True:
    user_input = input("Roll the dice? (y/n): ")
    # check if the input is valid
    if user_input.lower() == "y":
        # roll the dice
        roll_dice()
    elif user_input.lower() == "n":
        # if n, end the game
        break
    else:
        print("Invalid choice!")

# when the loop ends, thank user for playing!
print("Thanks for playing!")
