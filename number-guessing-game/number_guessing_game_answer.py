import random

number_to_guess = random.randint(1, 100)

while True:
    # to handle any errors, use try - except method with custom message
    # you can get the correct error to catch by trying to input incorrect, well, input
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        # this runs only if the guess is a number!
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else: 
            print('Congratulations! You guessed the number.')
            break

    except ValueError:
        print('Please enter a valid number')

# you can put the whole logic of the game inside the try block! . o .