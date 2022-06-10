def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == -1:
                # returns the first empty space in the sudoku puzzle
                return i, j
    # if all things in the board are filled
    return None, None


def isvalid(board, guess, row, col):
    if guess in board[row]:
        return False
    columnvals = []
    for i in range(9):
        columnvals.append(board[i][col])
    if guess in columnvals:
        return False
    # finding which third the guess is in
    row_start = (row//3) * 3
    col_start = (col//3) * 3
    for j in range(row_start, row_start + 3):
        for k in range(col_start, col_start + 3):
            if board[j][k] == guess:
                return False
    return True


def solve(board):
    row, col = find_empty(board)

    if row is None:
        return True
    for guess in range(1, 10):
        if isvalid(board, guess, row, col):
            board[row][col] = guess # changing if it is a valid input puzzle
            if solve(board):
                # once we have changed our puzzle to put in our new guess,
                # then we are just checking if the puzzle still works
                return True
        # if  guess was wrong, change it
        board[row][col] = -1
    return False


board = [[-1, -1, 7, 6, 2, -1, -1, -1, -1],
             [-1, -1, 8, -1, 3, -1, 6, -1, -1],
             [-1, 9, 2, 4, -1, 7, -1, -1, -1],

             [-1, -1, -1, -1, -1, -1, 2, -1, -1],
             [-1, -1, -1, -1, 7, -1, -1, 6, 1],
             [-1, -1, -1, -1, -1, -1, -1, 8, -1],

             [-1, 3, -1, -1, 4, -1, -1, 2, -1],
             [-1, 4, -1, -1, 6, 9, 8, -1, -1],
             [1, -1, -1, -1, -1, -1, -1, 4, 7]]
print(solve(board))
print(board)