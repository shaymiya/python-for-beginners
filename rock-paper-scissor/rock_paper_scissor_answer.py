# MORE ELOQUENT SOLUTION!
import random

# in python we have DICTIONARIES
# key -> value
emojis = { 'r': '🪨', 's': '✂️', 'p': '📜'} # make a dictionary for emojis
choices = ('r', 'p', 's') # make a list of valid choices! [] = open list, () = read only list!!

while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue # return back to the start of the loop!

    # with this the random picks one of the choices on the predefined list! SO CLEVER
    computer_choice = random.choice(choices) 

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'r') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win!')
    else:
        print('You lose')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break
    
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