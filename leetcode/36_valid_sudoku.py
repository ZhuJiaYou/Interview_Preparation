def is_valid_sudoku(board):
    return is_row_valid(board) and is_col_valid(board) and is_square_valid(board)


def is_row_valid(board):
    for row in board:
        if not is_unit_valid(row):
            return False
    return True


def is_col_valid(board):
    for col in zip(*board):  # NOTICE
        if not is_unit_valid(col):
            return False
    return True


def is_square_valid(board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_unit_valid(square):
                return False
    return True


def is_unit_valid(units):
    units = [c for c in units if c != '.']
    return len(set(units)) == len(units)


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(is_valid_sudoku(board))
