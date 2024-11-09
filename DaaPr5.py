def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        print_board(board)
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = '.'  # Backtrack
    return False

def n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists for the given board size.")

n = int(input("Enter the number of queens: "))
n_queens(n)
