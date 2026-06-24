"""
Number Guessing Game
Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low.

TODO:
- functional programming 
- a function to ask the minimum and maximum numbers 
- restrict user to enter only numbers
- use while loops 
- a function to serve as the front page of the game

"""
import random


def main():
    game_play = front_logic()
    print(game_play)

def number_guessing():
    
    attempt_made = 0
    total_attempt = 7

    while True:
        while True:
            try:
                minimum = int(input("Starting Number: \n")) 
                break
            except (ValueError, TypeError) as e:
                print(e, "enter valid number")
                continue
                
        
        while True:
            try:
                maximum = int(input("Ending Number: "))
                break
            except (ValueError, TypeError) as e:
                print(e, "enter valid number")
                continue
        if minimum >= maximum:
            print("Notice: minimum should be less than Maximum... Try Again")
            continue
        else:
            break 
    guess_number = random.randint(minimum,maximum)

    
    

    # front of the game

    while attempt_made < total_attempt:
        attempt_made += 1
        while True:
            try:
                choice = int(input("\nGuess the number: "))
                break
            except (ValueError, TypeError):
                print("enter valid input")
                continue
            
        if choice == guess_number:
            print(f"congratulations! its correct. you guessed the number in {attempt_made}attempts")
            print(f"you won ${attempt_made*100}")
            break
        elif choice < guess_number:
            print ("Too Low Try again")
        elif choice > guess_number:
            print("Too High! Try again")
    else:
        print(f"Sorry the guess number is {guess_number}\nyou have exhausted total attempt")
    return ""



def front_logic():

    message = input(f"\n{"*"*10} NUMBER GUESSING GAME {"*"*10} \npress 's' to START game or 'n' to EXIT game\n").strip().lower()

    match message:
        case 'n':
            print( "Program exited ... ")
            return
        case 's':

            counter = 1
            while counter < 50:
                number_guessing()
                print(f"you have played the game {counter}\n")
                counter +=1

                quit_game =input("\npress 'n' to quit game: or press any key to continue: \n")
                if quit_game == "n":
                    break
                else:
                    continue

if __name__ == "__main__":
    main()
