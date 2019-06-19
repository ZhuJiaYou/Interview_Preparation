def search_in_matrix(target: int, matrix: 'list[list[int]]') -> 'bool':
    row = 0
    col = len(matrix[0]) - 1
    while (row < len(matrix)) and (col >= 0):
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return True
    return False


if __name__ == '__main__':
    m = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(search_in_matrix(7, m))
    print(search_in_matrix(5, m))
    print(search_in_matrix.__annotations__)
