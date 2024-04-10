from rps3 import rps
from guess import guess
import sys



def play(name= "player 1"):
    welcomeBack = False
    while True:
        if welcomeBack == True:
            print(f"\n{name}, welcome back to the Arcade menu.")
        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n"
        )
        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play(name)

        welcomeBack = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess(name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")




if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    play(args.name)
# choose = input("\npress...\n 1 for Rock-Paper-Scissor \n 2 for Number Guess \n press x to exit")

# while True:
#     if choose not in ['1','2','x','X']:
#         continue
#     elif  int(choose) == 1:
#         rps3()
#     elif int(choose) == 2:
#         guess()
#     else:
#         break
     