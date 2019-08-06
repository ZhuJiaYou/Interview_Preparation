def longest_no_repeat(s):
    dic = {}
    for c in s:
        dic[c] = -1
    max_sub_len = 0
    now = 0
    for i in range(len(s)):
        if dic[s[i]] != -1 and i - dic[s[i]] <= now:
            if max_sub_len < now:
                max_sub_len = now
            now = i - dic[s[i]]
        else:
            now += 1
        dic[s[i]] = i
        # print(now, max_sub_len)
    if max_sub_len < now:
        max_sub_len = now
    return max_sub_len


if __name__ == '__main__':
    s = 'arabcacfr'
    print(longest_no_repeat(s))
    s = 'abba'
    print(longest_no_repeat(s))
    s = 'abcabcbb'
    print(longest_no_repeat(s))

    print("*******************")
    s = 'dvdf'
    print(longest_no_repeat(s))
