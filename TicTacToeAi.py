import math

# Function to print the current state of the board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to check if a player has won the game
def is_winner(board, player):
    # Check rows for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns for a win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(cell != '.' for row in board for cell in row)

# Function to evaluate the board and return a score
def evaluate(board):
    if is_winner(board, 'X'):
        return 10
    elif is_winner(board, 'O'):
        return -10
    return 0

# Minimax algorithm with alpha-beta pruning to find the best move
def min_max(board, depth, is_maximizing, alpha, beta, max_depth):
    score = evaluate(board)
    # If the game is over or max depth is reached, return the score
    if score == 10 or score == -10 or is_full(board) or depth == max_depth:
        return score
    
    if is_maximizing:
        best = -math.inf
        # Loop through all cells
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    best = max(best, min_max(board, depth + 1, False, alpha, beta, max_depth))
                    board[i][j] = '.'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        # Loop through all cells
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    best = min(best, min_max(board, depth + 1, True, alpha, beta, max_depth))
                    board[i][j] = '.'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# Function to find the best move for the AI
def find_best_move(board, max_depth):
    best_val = -math.inf
    best_move = (-1, -1)
    
    # Loop through all cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                move_val = min_max(board, 0, False, -math.inf, math.inf, max_depth)
                board[i][j] = '.'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    
    return best_move

# Main function to run the game
def main():
    board = [['.' for _ in range(3)] for _ in range(3)]
    player_choice = input("Choose your player (X/O): ").upper()
    while player_choice not in ['X', 'O']:
        player_choice = input("Invalid choice. Choose your player (X/O): ").upper()
    
    human = player_choice
    ai = 'O' if human == 'X' else 'X'
    
    # Inform the player about the difficulty range
    print("Enter the difficulty level (search depth) between 1 and 10:")
    max_depth = int(input("Enter the difficulty level (search depth): "))
    while max_depth < 1 or max_depth > 10:
        max_depth = int(input("Invalid choice. Enter the difficulty level (search depth) between 1 and 10: "))
    
    while not is_full(board) and not is_winner(board, 'X') and not is_winner(board, 'O'):
        print_board(board)
        row, col = map(int, input("Enter row and column (1-3): ").split())
        row -= 1  # Convert to 0-based index
        col -= 1  # Convert to 0-based index
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '.':
            board[row][col] = human
            if not is_full(board) and not is_winner(board, human):
                ai_move = find_best_move(board, max_depth)
                board[ai_move[0]][ai_move[1]] = ai
        else:
            print("Invalid move. Try again.")
    
    print_board(board)
    if is_winner(board, 'X'):
        print("X wins!")
    elif is_winner(board, 'O'):
        print("O wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()