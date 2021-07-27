board = [4, 0, 0, 0]
notes_board = [4, [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]


def remove_value(value, input_board):
    for i in range(0, len(input_board)):
        try:
            input_board.remove(value)
        except ValueError:
            break
    return input_board


resulting_board = remove_value(0, board)

print(resulting_board)
