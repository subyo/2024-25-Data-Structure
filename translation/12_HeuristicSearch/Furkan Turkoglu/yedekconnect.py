# Connect Four Oyunu

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
def make_move(board, col, player):
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
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Oyuncu {current_player}'in sırası:")
        col = int(input("Hangi sütuna oynamak istersiniz? (0-6): "))

        if col < 0 or col >= cols:
            print("Geçersiz hamle! Lütfen tekrar deneyin.")
            continue

        if not make_move(board, col, current_player):
            print("Bu sütun dolu! Lütfen başka bir sütun seçin.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Oyuncu {current_player} kazandı!")
            break

        if ' ' not in board[0]:
            print_board(board)
            print("Oyun berabere bitti!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
