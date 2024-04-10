import sys
import random

def guess(name = "palyer 1"):
    win =0
    gameCount = 0
    winPer=0
    name
    def guess_game():
     
        playerChoose = input(f"{name} Enter your Guess.. 1,2 or 3 ")
        player = int(playerChoose)
        if playerChoose not in ['1','2','3']:
            print(f"\n{name} choose number with in 1,2 or 3 ")
            guess_game()
        computerChoose = random.choice('123')
        computer = int(computerChoose)
        def find(player,computer):
            nonlocal win, gameCount, winPer
            gameCount+=1
            if player>computer:
                win+=1
                return (f"{name} you won 🥳")
            elif player == computer:
                return (f"Draw")
            else:
                return (f"{name} Python Won 🐍")
        result = find(player,computer)
        print(result)
        print(f"\n game count : {gameCount}")
        print(f"{name} won : {win}")
        print(f"{name} win Percentage :{((win/gameCount)*100):.2f}%")

        print(f"\n{name} want to play Again:")
        choose = input(f"\n Y for Yes \n Q for No")

        while True:
           if choose.lower() not in ['y','q']:
               continue
           else:
               break
        if choose.lower() == "y":
            return guess_game()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else :
                return


    return guess_game

if __name__ == "__main__":
    import argparse

    parse = argparse.ArgumentParser(
        description="Provide Personalized Game Experiance"
    )
    parse.add_argument(
        '-n','--name',metavar="name",required=True, help="name of the user in game"
    )
    args = parse.parse_args()
    
    guessNow = guess(args.name)
    guessNow()



