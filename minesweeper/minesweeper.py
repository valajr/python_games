from random import randrange

EMPTY = " "
BOMB = "x"
BRICK = "-"
START_ASC = 97

def run():
    high_points = 0
    high_winner = 0
    security_check = set()

    with open("hist_ms.txt", "a") as f:
        f.write("")

    with open("hist_ms.txt") as f:
        for line in f:
            if "," in line:
                line_winner, line_points = line.split(",")
                line_points = float(line_points[:-1])
                if(line_points > high_points):
                    high_points = line_points
                    high_winner = line_winner

    def generateBoard(size, bomb_qnt):
        board = size * size * [0]

        i = 0
        while i < bomb_qnt:
            i += 1
            bomb_pos = randrange(0, size * size)
            if board[bomb_pos] != BOMB:
                board[bomb_pos] = BOMB
            else:
                i -= 1

        for i in range(len(board)):
            if board[i] == BOMB:
                if i%size - 1 >= 0:
                    if board[i - 1] != BOMB:
                        board[i - 1] += 1

                if i%size + 1 < size:
                    if board[i + 1] != BOMB:
                        board[i + 1] += 1
                        
                if i >= size:
                    if board[i - size] != BOMB:
                        board[i - size] += 1

                    if i%size - 1 >= 0:
                        if board[i - 1 - size] != BOMB:
                            board[i - 1 - size] += 1

                    if i%size + 1 < size:
                        if board[i + 1 - size] != BOMB:
                            board[i + 1 - size] += 1

                if int(i/size) != size - 1:
                    if board[i + size] != BOMB:
                            board[i + size] += 1

                    if i%size - 1 >= 0:
                        if board[i - 1 + size] != BOMB:
                            board[i - 1 + size] += 1

                    if i%size + 1 < size:
                        if board[i + 1 + size] != BOMB:
                            board[i + 1 + size] += 1

        for i in range(len(board)):
            if board[i] == 0:
                board[i] = BRICK
        
        return board

    def printScores(board, size):
        points = 0
        for i in range(size * size):
            if board[i] != EMPTY:
                points += 1
        
        print(f"Highscore: {high_points}      Score: {points}")

    def printLineX(size):
        alphabet = " "
        for i in range(START_ASC, START_ASC + size):
            alphabet += chr(i)
        for letter in alphabet:
            print(f" {letter}  ", end = ' ')
        print()

    def showBoard(board, size):
        y = 0
        printScores(board, size)
        printLineX(size)
        for c in range(0, size*size, size):
            y += 1
            if y < 10:
                print(y, end = '   ')
            elif y < 100:
                print(y, end = '  ')
            else:
                print(y, end = ' ')


            for i in range(size):
                print('| ', end = '')
                print(board[c + i], end = ' |')
            print()
        print("\n")

    def  isValidPlay(size, x, y, position):
        if x > (size - 1) or x < 0:
            return False
        if y > size or y < 0:
            return False
        if position > size * size or position < 0:
            return False
        for i in security_check:
            if position == i:
                return False
        return True

    def play():
        valid_play = False
        while not valid_play:
            x, y = input("Tipe the position to play: ").split(" ")
            x = ord(x) - START_ASC
            y = int(y)
            position = x + (int(y) - 1) * size
            if isValidPlay(size, x, y, position):
                valid_play = True
            else:
                print("Invalid position!\n")

        return position

    def seeSides(position, board, size):
        for i in security_check:
            if position == i:
                return security_check
        
        security_check.add(position)

        if position%size - 1 >= 0:
            if board[position - 1] == BRICK:
                seeSides(position - 1, board, size)
            elif board[position - 1] != BOMB:
                security_check.add(position - 1)

        if position%size + 1 < size:
            if board[position + 1] == BRICK:
                seeSides(position + 1, board, size)
            elif board[position + 1] != BOMB:
                security_check.add(position + 1)
                
        if position >= size:
            if board[position - size] == BRICK:
                seeSides(position - size, board, size)
            elif board[position - size] != BOMB:
                security_check.add(position - size)

            if position%size - 1 >= 0:
                if board[position - 1 - size] == BRICK:
                    seeSides(position - 1 - size, board, size)
                elif board[position - 1 - size] != BOMB:
                    security_check.add(position - 1 - size)

            if position%size + 1 < size:
                if board[position + 1 - size] == BRICK:
                    seeSides(position + 1 - size, board, size)
                elif board[position + 1 - size] != BOMB:
                    security_check.add(position + 1 - size)
        
        if int(position/size) != size - 1:
            if board[position + size] == BRICK:
                seeSides(position + size, board, size)
            elif board[position + size] != BOMB:
                security_check.add(position + size)

            if position%size - 1 >= 0:
                if board[position - 1 + size] == BRICK:
                    seeSides(position - 1, board, size)
                elif board[position - 1 + size] != BOMB:
                    security_check.add(position - 1 + size)

            if position%size + 1 < size:
                if board[position + 1 + size] == BRICK:
                    seeSides(position + 1 + size, board, size)
                elif board[position + 1 + size] != BOMB:
                    security_check.add(position + 1 + size)

    def upd(position, visible_board, board, size):
        if board[position] == "-":
            seeSides(position, board, size)
            for i in security_check:
                visible_board[i] = board[i]
        else:
            visible_board[position] = board[position]
            security_check.add(position)

        return visible_board

    winner = 0
    points = 0
    size = int(input("Type the number of lines/columns: "))
    bomb_qnt = int(input("Type the number of bombs: "))
    board = generateBoard(size, bomb_qnt)
    visible_board = [EMPTY] * size * size
    showBoard(visible_board, size)

    while not winner:
        if len(security_check) == size * size - bomb_qnt:
            winner = 2

        else:
            position = play()
            if board[position] == BOMB:
                winner = 1
            visible_board = upd(position, visible_board, board, size)
            showBoard(visible_board, size)

    for i in range(size * size):
        if board[i] == BOMB:
            visible_board[i] = board[i]
    showBoard(visible_board, size)

    for i in range(size * size):
        if visible_board[i] != EMPTY:
            points += 1

    if winner == 1:
        points = points/2
        print(f"You lose! :('       Score: {points}")

    if winner == 2:
        print(f"Nice play! You won.         Score: {points}")
        
    with open("hist_ms.txt", "a") as f:
        f.write(f"{winner},{points}\n")


if __name__ == '__main__':
    run()