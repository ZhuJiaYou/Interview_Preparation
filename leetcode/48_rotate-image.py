def rotate(matrix):
    matrix[:] = zip(*matrix[::-1])


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print(matrix)

