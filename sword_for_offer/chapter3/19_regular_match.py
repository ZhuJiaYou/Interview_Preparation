def match(s, pattern):
    if not pattern:
        return not s
    f_match = bool(s) and pattern[0] in [s[0], '.']
    if len(pattern) > 1 and pattern[1] == '*':
        return (match(s, pattern[2:])) or (f_match and match(s[1:], pattern))
    else:
        return f_match and match(s[1:], pattern[1:])
    return True


def match2(s: str, p: str) -> bool:
    dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
    dp[-1][-1] = True

    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            f_match = i < len(s) and p[j] in [s[i], '.']
            if j + 1 < len(p) and p[j+1] == '*':
                dp[i][j] = dp[i][j+2] or (f_match and dp[i+1][j])
            else:
                dp[i][j] = f_match and dp[i+1][j+1]
    return dp[0][0]



if __name__ == '__main__':
    print(match2("aa", "a*"))  # T

