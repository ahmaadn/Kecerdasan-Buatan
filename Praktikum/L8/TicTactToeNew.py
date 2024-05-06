import random

def get_valid_moves(board) :
    # Fungsi untuk mendapatkan daftar langkah yang valid
    valid_moves = []
    for i in range(len(board)) :
        if board[i] == " ":
            valid_moves.append(i)
    return valid_moves

def minimax(board, player, depth=0):
# Fungsi untuk mengevaluasi nilai setiap langkah menggunakan algoritma minimax
    if check_win(board, "x"):
        return -10 + depth
    elif check_win(board, "0"):
        return 10 - depth
    elif " " not in board:
        return 0

    if player == "0":
        best_score = float("-inf")
        for move in get_valid_moves(board):
            new_board = board[ : ]
            new_board[move] = player
            score = minimax(new_board, "x", depth + 1)
            best_score = max(best_score, score)
            return best_score
    else:
        best_score = float("inf")
        for move in get_valid_moves(board) :
            new_board = board[ : ]
            new_board[move] = player
            score = minimax(new_board, "O", depth + 1)
            best_score = min(best_score, score)
        return best_score

def get_best_move(board, player):
# Fungsi untuk mendapatkan langkah terbaik menggunakan algoritma minimax
    best_score = float("-inf") if player == "0" else float("inf")
    best_move = None
    for move in get_valid_moves(board) :
        new_board = board[ : ]
        new_board[move] = player
        score = minimax(new_board, "x" if player == "0" else "0")
        if player == "0" and score > best_score:
            best_score = score
            best_move = move
        elif player == "x" and score < best_score:
            best_score = score
            best_move = move
    return best_move


def draw_board(board):
    """
    Fungsi untuk menggambar papan permainan
    """
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board, player):
    """
    Fungsi untuk memeriksa apakah seorang pemain menang
    """
    win_positions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for positions in win_positions:
        if board[positions[0]] == player and board[positions[1]] == player and board[positions[2]] == player:
            return True
    return False


def tic_tac_toe():
# Fungsi untuk menjalankan permainan Tic Tac Toe
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["x", "o"]
    turn = random.choice([0, 1])
    while True:
        draw_board(board)
        print("Player " + players[turn] + "'s turn.")
        
        if players[turn] == "x":
            move = int(input("Enter move (0-8): "))
            if board[move] != " ":
                print("Invalid move. Try again.")
                continue
        else:
            move = get_best_move(board, "0")
        board [move] = players[turn]

        if check_win(board, players[turn]):
            draw_board(board)
            print("player " + players[turn] + " wins!")
            break
        
        if " " not in board:
            draw_board(board)
            print("It's a tie!")
            break
        turn = (turn + 1) % 2

if __name__ == "__main__":
    tic_tac_toe()
