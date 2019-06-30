def exist_(board: 'list[list[str]]', word: str) -> bool:
    def go_on(i, j, path, word):
        if len(word) == 0:
            return True
        for (a, b) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= a < len(board) and 0 <= b < len(board[0]) and (not path[a][b]) and \
                    board[a][b] == word[0]:
                path[a][b] = True
                print("A, B == {0}, {1}".format(a, b))
                print(path)
                if go_on(a, b, path, word[1:]):
                    return True
                else:
                    path[a][b] = False
        return False

    if len(board) == 0 and len(word) > 0:
        return False
    elif len(board) * len(board[0]) < len(word):
        return False
    elif len(word) == 0:
        return True
    else:
        path = []
        for _ in range(len(board)):
            path.append([False]*len(board[0]))

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                print("I, J == {0}, {1}".format(i, j))
                path[i][j] = True
                if go_on(i, j, path, word[1:]) == True:
                    return True
                path[i][j] = False

    return False


if __name__ == '__main__':
    print(exist_([["C", "A", "A"],
                  ["A", "A", "A"],
                  ["B", "C", "D"]], "AAB"))
