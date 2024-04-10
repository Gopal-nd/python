import sys
import random
from enum import Enum

playAgain = True

while playAgain:
    playerChoise = input("ENTER....\n 1 for ROCK \n 2 for PAPER \n 3 for SCISSORS\n\n")
    
    player = int(playerChoise)
    if player not in [1,2,3]:
        print("\n"+ playerChoise+" is not valid  \n1 for ROCK \n 2 for PAPER \n 3 for SCISSORS\n\n ")
        sys.exit()
    computerChoise = random.choice('123')
    computer = int(computerChoise)

    if player == 1 and computer ==3:
        print("You won!🥳")
    elif player == 2 and computer == 1:
        print("You won!🥳")
    elif player == 3 and computer == 2:
        print("You won!🥳")
    elif player == computer:
        print('Draw 😊')
    else:
        print('Python won 🐍')

    choice = input("\n\nEnter ...\n y to PalyAgain \n Q to Quit")
    if choice.lower() == 'y':
        continue
    else:
        print("Thank You for Playing ! \n Good bye👋")
        sys.exit()