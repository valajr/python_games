def run():
    ended = False

    def checkWinner(board):
        if board[0] == board[1] and board[1] == board[2] and board[0] != '|   |':
            return board[0], True
        elif board[3] == board[4] and board[4] == board[5] and board[3] != '|   |':
            return board[3], True
        elif board[6] == board[7] and board[7] == board[8] and board[6] != '|   |':
            return board[6], True

        elif board[0] == board[4] and board[4] == board[8] and board[0] != '|   |':
            return board[0], True
        elif board[2] == board[4] and board[4] == board[6] and board[2] != '|   |':
            return board[2], True

        elif board[0] == board[3] and board[3] == board[6] and board[0] != '|   |':
            return board[0], True
        elif board[1] == board[4] and board[4] == board[7] and board[1] != '|   |':
            return board[1], True
        elif board[2] == board[5] and board[5] == board[8] and board[2] != '|   |':
            return board[2], True
        return 'Ninguém', False

    board = ['|   |', '|   |', '|   |', '|   |', '|   |', '|   |', '|   |', '|   |', '|   |']
    winner = 'Ninguém'
    i = 0

    while not ended:
        i += 1
        if i%2:
            player = 1
            plays = int(input(f"Player {player} choose one number in 1 to 9: "))
            if board[plays - 1] == '| 1 |' or board[plays - 1] == '| 2 |':
                print("Invalid position")
                i -= 1
            else:
                board[plays - 1] = '| 1 |'
                for place in range(0, 9, 3):
                    print(board[place], board[place+1], board[place+2])
            winner, ended = checkWinner(board)
            
        else:
            player = 2
            plays = int(input(f"Player {player} choose one number in 1 to 9: "))
            if board[plays - 1] == '| 1 |' or board[plays - 1] == '| 2 |':
                print("Invalid position")
                i -= 1
            else:
                board[plays - 1] = '| 2 |'
                for place in range(0, 9, 3):
                    print(board[place], board[place+1], board[place+2])
            winner, ended = checkWinner(board)

    print(f"Congratulations, player {winner}")

if __name__ == '__main__':
    run()