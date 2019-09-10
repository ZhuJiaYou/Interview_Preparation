def land_num(grid):
    def mark(i, j):
        grid[i][j] = '2'
        if i+1 < len(grid) and grid[i+1][j] == '1':
            mark(i+1, j)
        if j+1 < len(grid[0]) and grid[i][j+1] == '1':
            mark(i, j+1)
        if i-1 >= 0 and grid[i-1][j] == '1':
            mark(i-1, j)
        if j-1 >= 0 and grid[i][j-1] == '1':
            mark(i, j-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                mark(i, j)
                print(grid)
    return count


if __name__ == '__main__':
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(land_num(grid))
