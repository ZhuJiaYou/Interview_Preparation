def movingCount(threshold, rows, cols):
    if rows == 0 or cols == 0:
        return 0
    else:
        history = []
        for _ in range(rows):
            history.append([False]*cols)

    def pos_sum(a):
        s = 0
        while a != 0:
            s += (a % 10)
            a = a // 10
        return s

    count = 0

    def move(i, j):
        for (a, b) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if (0 <= a < rows) and (0 <= b < cols) and (not history[a][b]) \
                    and ((pos_sum(a) + pos_sum(b)) <= threshold):
                nonlocal count
                count += 1
                history[a][b] = True
                print(history)
                print((pos_sum(a) + pos_sum(b)))
                move(a, b)

    history[0][0] = True
    count += 1
    move(0, 0)
    return count

 
def movingCount2(threshold, rows, cols):
    if rows == 0 or cols == 0:
        return 0
    else:
        history = [[False]*cols for _ in range(rows)]

    def pos_sum(a):
        s = 0
        while a != 0:
            s += (a % 10)
            a = a // 10
        return s

    def move(i, j):
        if (pos_sum(i) + pos_sum(j)) <= threshold:
            history[i][j] = True
            for (a, b) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (0 <= a < rows) and (0 <= b < cols) and (not history[a][b]):
                    move(a, b)

    move(0, 0)
    return sum(sum(history, []))


if __name__ == '__main__':
    print(movingCount2(2, 3, 4))
