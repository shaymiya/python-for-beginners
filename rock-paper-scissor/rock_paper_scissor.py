# ROCK-PAPER-SCISSORS
# // start loop
# 1. ask player to choose rock paper or scissors (r/p/s)
# 2. check if the answer is valid -> if not, print invalid choice!
# 3. if answer is valid, print player's choice with an emoji: You chose 🪨
# 4. randomize computer's pick and print it wiht an emoji: Computer chose 📜
# 5. check if the player won: You win / You lose
# 6. ask if the player wants to continue: Continue (y/n)
# 7. y restarts the loop, n exits the program

import random

# make a function for computer's choice
def computer_chose():
    computer_chose = random.randint(1,3)

    # print computer's choice
    if computer_chose == 1:
        print("Computer chose 🪨")
    elif computer_chose == 2:
        print("Computer chose 📜")
    else:
        print("Computer chose ✂️")

    return computer_chose

# make a function for converting player's choise to emoji
def player_chose(choice):
    if choice == "r":
        print("You chose 🪨")
    elif choice == "p":
        print("You chose 📜")
    else:
        print("You chose ✂️")
    

# make a function for checking the winner : r = 1, p = 2, s = 3
def check_winner(player, computer):
    if player == "r":
        if computer == 1:
            print("It's a tie!")
        elif computer == 2:
            print("You lose")
        else:
            print("You win!")
    elif player == "p":
        if computer == 1:
            print("You win!")
        elif computer == 2:
            print("It's a tie!")
        else:
            print("You lose")
    else:
        if computer == 1:
            print("You lose")
        elif computer == 2:
            print("You win!")
        else:
            print("It's a tie!")

playing = True
player_input = ""

# test the program
while True:
    while playing:
        player_input = input('Rock, paper, or scissors? (r/p/s): ')
        if player_input == "r" or player_input == "p" or player_input == "s":
            player_chose(player_input)
            check_winner(player_input, computer_chose())
            break
        else:
            print('Invalid choice!')

    continue_game = input("Continue? (y/n): ")

    if continue_game == 'n':
        break
    elif continue_game != 'y':
        playing = False
        print("Invalid choice!")
    else:
        playing = True
