ROCK = 0
PAPER = 1
SCISSORS = 2

def run():
    played = [0, 0, 0]

    with open("hist_jokenpo.txt", "a") as f:
        f.write("")

    with open("hist_jokenpo.txt") as f:
        rock = 0
        paper = 0
        scissors = 0
        for line in f:
            if "," in line:
                line_rock, line_paper, line_scissors = line.split(",")
                rock += int(line_rock)
                paper += int(line_paper)
                scissors += int(line_scissors[:-1])
        played[ROCK] = rock
        played[PAPER] = paper
        played[SCISSORS] = scissors
        
    def showPossibilities(played, played_now):
        rock = played[ROCK] + played_now[ROCK]
        paper = played[PAPER] + played_now[PAPER]
        scissors = played[SCISSORS] + played_now[SCISSORS]
        total = rock + paper + scissors
        if total != 0:
            print(f"Chance of rock: {round((rock/total), 2) * 100}%\t", end='')
            print(f"Chance of paper: {round((paper/total), 2) * 100}%\t", end='')
            print(f"Chance of scissors: {round((scissors/total), 2) * 100}%")
        else:
            print("Chance of rock: 0\tChance of paper: 0\tChance of scissors: 0")

    def isValidPlay(move):
        if int(move) in [ROCK, PAPER, SCISSORS]:
            return True
        else:
            print("Invalid move!")
            return False

    def play(player):
        while True:
            print(f"Make your move, player {player}: ", end='')
            move = int(input()) - 1
            if isValidPlay(move):
                    return(move)

    def compare(move_1, move_2):
        if move_1 == ROCK:
            if move_2 == PAPER:
                return move_2
            if move_2 == SCISSORS:
                return move_1
        elif move_1 == PAPER:
            if move_2 == ROCK:
                return move_1
            if move_2 == SCISSORS:
                return move_2
        else:
            if move_2 == ROCK:
                return move_2
            if move_2 == PAPER:
                return move_1

    empate = True
    played_now = [0, 0, 0]
    player = [1, 2]
    moves = []

    print("1. Rock\n2. Paper\n3. Scissor")

    while empate:
        showPossibilities(played, played_now)
        moves.append(play(player[0]))
        moves.append(play(player[1]))
        
        if moves[-1] != moves[-2]:
            winner = compare(moves[-1], moves[-2])
            if winner == moves[-1]:
                print(f"Congratulations, player {player[1]}")
            if winner == moves[-2]:
                print(f"Congratulations, player {player[0]}")
            empate = False

    for move in moves:
        if move == ROCK:
            played_now[ROCK] += 1
        elif move == PAPER:
            played_now[PAPER] += 1
        elif move == SCISSORS:
            played_now[SCISSORS] += 1

    with open("hist_jokenpo.txt", "a") as f:
        f.write(f"{played_now[ROCK]},{played_now[PAPER]},{played_now[SCISSORS]}\n")


if __name__ == '__main__':
    run()