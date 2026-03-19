# NUMBER GUESSING GAME
# 1. Generate a number between 1-100
# 2. Ask the user to guess the number (input) -> if anything else than an int is given, print Please enter a valid number
# 3. Compare the input with the generated number
# 4. If the guess is too high, print Too high!, if too low print Too low!
# 5. If the user guesses correctly print Congratulations! You guessed the number.
# 6. End the game

# import the random module for random number generation
import random

# generate a random number 1-100 for the game
number_to_guess = random.randint(1, 100)

# use while loop for the game loop
while True:
    # ask the user to guess the number
    guess = input("Guess the number between 1 and 100: ")

    # check if the input is valid (isdigit() for integers)
    if guess.isdigit():
        if number_to_guess > int(guess):
            print("Too low!")
        elif number_to_guess < int(guess):
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break
    # if the input is anything else than an integer, print the following:
    else: 
        print("Please enter a valid number")
