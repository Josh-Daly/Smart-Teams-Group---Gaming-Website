import random

SIZE = 3
PLAYER = 'X'
COMPUTER = 'O'

# 3x3 board filled with spaces
board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]


def reset_board():
    for i in range(SIZE):
        for j in range(SIZE):
            board[i][j] = ' '


def print_board():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print()


def check_free_space():
    free_spaces = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == ' ':
                free_spaces += 1
    return free_spaces


def player_move():
    while True:
        try:
            x = int(input("Enter row number (1-3): ")) - 1
            y = int(input("Enter column number (1-3): ")) - 1

            if x < 0 or x >= SIZE or y < 0 or y >= SIZE or board[x][y] != ' ':
                print("Invalid Move!")
            else:
                board[x][y] = PLAYER
                break
        except ValueError:
            print("Please enter a valid number!")


def computer_move():
    if check_free_space() > 0:
        while True:
            x = random.randint(0, SIZE - 1)
            y = random.randint(0, SIZE - 1)
            if board[x][y] == ' ':
                board[x][y] = COMPUTER
                break


def check_winner():
    # Rows and columns
    for i in range(SIZE):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return ' '


def print_winner(winner):
    if winner == PLAYER:
        print("YOU WIN!!")
    elif winner == COMPUTER:
        print("YOU LOSE!!")
    else:
        print("IT'S A DRAW!!")


def main():
    winner = ' '
    reset_board()

    while winner == ' ' and check_free_space() != 0:
        print_board()
        player_move()
        winner = check_winner()
        if winner != ' ' or check_free_space() == 0:
            break

        computer_move()
        winner = check_winner()

    print_board()
    print_winner(winner)


if __name__ == "__main__":
    main()
