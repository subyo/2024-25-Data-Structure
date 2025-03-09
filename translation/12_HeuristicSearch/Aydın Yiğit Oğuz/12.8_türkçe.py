import random
import time

# Oyun tahtası oluşturma
def create_board(rows, cols):
    board = []
    for _ in range(rows):
        row = [' '] * cols
        board.append(row)
    return board

# Oyun tahtasını ekrana yazdırma
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * len(row) * 2)

# Oyuncunun hamlesini yapma
def player_move(board, col, player):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return True
    return False

# Bilgisayarın hamlesini yapma
def computer_move(board, player):
    time.sleep(2)
    valid_moves = [col for col in range(len(board[0])) if ' ' in board[-1][col]]
    col = random.choice(valid_moves)
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return True

    return False


# Kazananı kontrol etme
def check_winner(board, player):
    # Dikey kontrol
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # Yatay kontrol
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # Çapraz kontrol (soldan sağa)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    # Çapraz kontrol (sağdan sola)
    for row in range(len(board) - 3):
        for col in range(3, len(board[0])):
            if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == player and board[row + 3][col - 3] == player:
                return True

    return False

# Oyunu başlatma
def play_game():
    rows = 6
    cols = 7
    board = create_board(rows, cols)
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        print_board(board)

        if current_player == 'X':
            print("Sıra sizde!")
            print("Lütfen bir sütun seçin (0-6):")
            col = int(input())

            if col < 0 or col >= cols or board[0][col] != ' ':
                print("Geçersiz hamle! Lütfen tekrar deneyin.")
                continue

            player_move(board, col, current_player)

        else:
            print("Bilgisayar düşünüyor...")
            computer_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Tebrikler! Oyuncu {current_player} kazandı!")
            break

        if all(board[0][col] != ' ' for col in range(cols)):
            print_board(board)
            print("Oyun berabere bitti!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

play_game()
