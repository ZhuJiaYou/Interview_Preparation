def spiral_order(matrix):
    ret = []
    while matrix:
        if matrix:
            ret += matrix.pop(0)
        print(matrix)
        for lst in matrix:
            if lst:
                ret.append(lst.pop())
            else:
                matrix.pop(0)
        print(matrix)
        if matrix:
            ret += matrix.pop()[::-1]
        print(matrix)
        for lst in matrix[::-1]:
            if lst:
                ret.append(lst.pop(0))
            else:
                matrix.pop()
        print(matrix)
    return ret

                
def spiral_order2(matrix):
    return list(matrix.pop(0)) + spiral_order2(list(zip(*matrix))[::-1]) if matrix else matrix


if __name__ == '__main__':
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(spiral_order2(m))
