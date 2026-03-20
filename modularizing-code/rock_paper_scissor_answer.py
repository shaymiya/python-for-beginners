# MORE ELOQUENT SOLUTION!
import random

# use UPPER CASE LETTERS to define constants!
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

# use ctrl + d to select all instances of 'r' + esc x 2 to cancel multi editing

# DRY-principle = Don't Repeat Yourself
emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📜'} # make a dictionary for emojis
choices = tuple(emojis.keys()) # make a list from a tuple of emoji dictionary!

def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice # acts as a break!
        else:
            print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == ROCK) or
        (user_choice == PAPER and computer_choice == ROCK)):
        print('You win!')
    else:
        print('You lose')

def play_game():
    while True:
        user_choice = get_user_choice()
        
        # with this the random picks one of the choices on the predefined list! SO CLEVER
        computer_choice = random.choice(choices) 

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()

# -------------------------------
# Ask the user to make a choice
# If choice is not valid
#   Print an error
# Let the computer make a choice
# Print choices (emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
#   Terminate