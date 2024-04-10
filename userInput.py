import sys
import random

# value = input("Please enter a value: \n")
# print(value)


print(("wlcome to game".upper().center(30,"-")))
PlayerChoise = input("Enter....\n 1 for Rock \n 2 for Paper \n 3 for Sisssore\n\n")

player = int(PlayerChoise)

if player not in [1, 2, 3]:
    sys.exit("you must enter the values in between 1 ,2,3")

computerchoice = random.choice("123")

computer = int(computerchoice)
print(computer)
print('')
print("your choose "+ PlayerChoise+'.' )
print('python choose '+ computerchoice +'.')
print('\n')

# if player == computer:
#     print("draw!")
# elif player > computer:
#     print("Congrats! You won:)")
# else:
#     print("Computer won")

if player == 1 and computer == 3:
    print("You win🥳")
elif player == 2 and computer == 2:
    print("You Win🥳")
elif player == 3 and computer ==2:
    print("Python win!🐍")
elif player == computer:
    print("Draw!😁")
else:
    print("Python Win!🐍")