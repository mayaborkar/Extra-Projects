def iswin(board):
    sumCol = 0
    for i in range(0, board.length):
        for j in range(0, board[i].length):
            sumCol += board[i][j]
        if sumCol == 45:
            return True
    return False


board = [4, 0, 0, 0], [0, 0, 2, 4], [1, 0, 4, 2], [0, 4, 3, 0]

notes_board = [4, 0, 0, 0], [0, 0, 2, 4], [1, 0, 4, 2], [0, 4, 3, 0]

notes = [1, 2, 3, 4]
row = []
column = []
temp = []


for i in range(0, 4):
    for j in range(0, 4):
        if board[i][j] == 0:
            notes_board[i][j] = notes

for i in range(0, 4):
    print(notes_board[i])

print(board)

for i in range(0, 4):
    temp = []
    for j in range(0, 4):
        if board[i][j] != 0:
            temp.append(board[i][j])
    row.append(temp)
print(row)

for i in range(0, 4):
    temp = []
    for j in range(0, 4):
        if board[j][i] != 0:
            temp.append(board[j][i])
    column.append(temp)
print(column)

'''
create 2 arrays one with first row of the board and the notes board only the first row remove the 4 from the notes board
'''








