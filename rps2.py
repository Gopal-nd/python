import sys
import random
from enum import Enum

game_count = 0
won = 0
loss = 0
draw = 0


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
    )
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("You Choos" + str(RPS(player)).replace("RPS.", "").title() + ".")
    print("Python Choos" + str(RPS(computer)).replace("RPS.", "").title() + ".")

    def decide_winner(player, computer):
        global game_count, won, loss, draw
        if player == 1 and computer == 3:
            won+=1
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            won+=1
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            won+=1
            return "🎉 You win!"
        elif player == computer:
            draw +=1
            return "😲 Tie game!"
        else:
            loss +=1
            return "🐍 Python wins!"
        
    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count, won, loss, draw
    game_count+=1
    print("\nGame Count: "+str( game_count))
    print("Won Count: "+str(won))
    print("Loss Count: "+str(loss))
    print("Draw Count: "+str(draw))

    print("\n Play again")

    while True:
        playagain = input('\n Y for Yes or \n Q for Quit')
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break

    if playagain.lower() == 'y':
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")

play_rps()