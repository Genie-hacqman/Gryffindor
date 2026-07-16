# using functions to practice loops and conditions to create a simple game called rock paper scissors.

import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_win = 0
    computer_win = 0
    draw = 0

    while True:
        user = input("Rock / Paper / Scissors (q to quit): ").lower()

        if user == "q":
            break

        if user not in options:
            print("wrong choice. Try again.")
            continue

        computer = random.choice(options)
        print("Computer chose:", computer)

        if user == computer:
            print("Draw")
            draw += 1

        elif (
            (user == "rock" and computer == "scissors") or
            (user == "paper" and computer == "rock") or
            (user == "scissors" and computer == "paper")
        ):
            print("You win")
            user_win += 1

        else:
            print("You lose")
            computer_win += 1

        print("Score -> You:", user_win, 
              "Computer:", computer_win, 
              "Draws:", draw)
        print()

    print("Final Score")
    print("You won:", user_win)
    print("Computer won:", computer_win)
    print("Draws:", draw)

if __name__ == "__main__":
    play_game()