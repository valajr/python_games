import jokenpo.jokenpo as jokenpo
import minesweeper.minesweeper as minesweeper
import tictactoe.tictactoe as tictactoe

def clear():
    print("\n"*20)

while True:
    clear()
    game = input("Choose your game:\n1. Jokenpo\n2. Minesweeper\n3. Tictactoe\n")
    clear()

    if game == '1':
        jokenpo.run()
    elif game == '2':
        minesweeper.run()
    elif game == '3':
        tictactoe.run()
    else:
        break
    input()