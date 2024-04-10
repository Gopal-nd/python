# clousre a function having to the scope of its parents  functionafter the parent function returned

def play(name):
    coins = 3
    def playGame():
        nonlocal coins
        coins -=1
        if coins >0:
            print(name+ ' have '+str(coins)+' coins')
    return playGame
run =play("go")
run()