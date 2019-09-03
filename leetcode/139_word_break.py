def word_break(s, words):
    def search(ss):
        if not ss:
            return True
        flag = False
        for i in range(1, len(ss)+1):
            if ss[:i] in words:
                if search(ss[i:]):
                    flag = True
        return True if flag else False
    return search(s)


def word_break2(s, words):
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i:j+1] in words:
                dp[j+1] = True
    return dp[-1]


if __name__ == '__main__':
    s = "applepenapple"
    words = ["apple", "pen"]
    print(word_break2(s, words))
    s = "catsandog"
    words = ["cats", "dog", "sand", "and", "cat"]
    print(word_break2(s, words))
    s = "leetcode"
    words = ["leet", "code"]
    print(word_break2(s, words))
