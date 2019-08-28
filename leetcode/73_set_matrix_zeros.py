def set_matrix_zeros(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in rows:
        matrix[i] = [0] * len(matrix[0])
    for j in cols:
        for i in range(len(matrix)):
            matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [
              [0,1,2,0],
              [3,4,5,2],
              [1,3,1,5]
             ]
    set_matrix_zeros(matrix)
    print(matrix)
