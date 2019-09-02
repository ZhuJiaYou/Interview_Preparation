def solve(board):
    if not board:
        return board
    m, n = len(board), len(board[0])
    stack = []
    for i in (0, m-1):
        for k in range(n):
            if board[i][k] == 'O':
                board[i][k] = 'A'
                stack.append((i, k))
    for j in (0, n-1):
        for k in range(1, m-1):
            if board[k][j] == 'O':
                board[k][j] = 'A'
                stack.append((k, j))
    while stack:
        i, j = stack.pop()
        if i-1 >= 0 and board[i-1][j] == 'O':
            board[i-1][j] = 'A'
            stack.append((i-1, j))
        if i+1 < m and board[i+1][j] == 'O':
            board[i+1][j] = 'A'
            stack.append((i+1, j))
        if j-1 >= 0 and board[i][j-1] == 'O':
            board[i][j-1] = 'A'
            stack.append((i, j-1))
        if j+1 < n and board[i][j+1] == 'O':
            board[i][j+1] = 'A'
            stack.append((i, j+1))
    for i in range(0, m):
        for j in range(0, n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'A':
                board[i][j] = 'O'


if __name__ == '__main__':
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']
            ]
    board2 = [["O", "X", "X", "O", "X"],
              ["X", "O", "O", "X", "O"],
              ["X", "O", "X", "O", "X"],
              ["O", "X", "O", "O", "O"],
              ["X", "X", "O", "X", "O"]
             ]
    solve(board)
    print(board)
