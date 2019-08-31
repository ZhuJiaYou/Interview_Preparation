def generate(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    triangle = [[1], [1, 1]]
    row = [1]
    for _ in range(numRows-2):
        for i in range(len(triangle[-1])-1):
            row.append(triangle[-1][i]+triangle[-1][i+1])
        row.append(1)
        triangle.append(row)
        row = [1]
    return triangle
