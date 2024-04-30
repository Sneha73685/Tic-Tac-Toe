def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Let's play Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input("Player {} - Enter row (0, 1, 2): ".format(players[current_player])))
        col = int(input("Player {} - Enter column (0, 1, 2): ".format(players[current_player])))

        if board[row][col] == ' ':
            board[row][col] = players[current_player]
            print_board(board)

            if check_winner(board, players[current_player]):
                print("Player {} wins!".format(players[current_player]))
                break
            elif check_draw(board):
                print("It's a draw!")
                break
            else:
                current_player = (current_player + 1) % 2
        else:
            print("That cell is already taken. Try again.")

if __name__ == "__main__":
    play_game()