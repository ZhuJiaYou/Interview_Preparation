def unique_paths(m, n):
    dp = [[0]*n for _ in range(m)]
    for j in range(n):
        dp[0][j] = 1
    for i in range(m):
        dp[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


if __name__ == '__main__':
    print(unique_paths(32, 28))
