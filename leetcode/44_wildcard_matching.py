def is_match(s, p):
    matches = [[False]*(len(p)+1) for _ in range(len(s)+1)]
    matches[0][0] = True
    for j in range(1, len(p)+1):
        if p[j-1] != '*':
            break
        matches[0][j] = True
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                matches[i][j] = matches[i-1][j] or matches[i][j-1]
            else:
                matches[i][j] = matches[i-1][j-1] and (p[j-1] in (s[i-1], '?'))
    print(matches)
    return matches[-1][-1]


if __name__ == '__main__':
    print("{} - {}".format(is_match("abc", "abc"), is_match2("abc", "abc")))  # T
    # print("{} - {}".format(is_match("abc", "a?c"), is_match2("abc", "a?c")))  # T
    # print("{} - {}".format(is_match("ac", "a?c"), is_match2("ac", "a?c")))  # F
    # print("{} - {}".format(is_match("aac", "a?c"), is_match2("aac", "a?c")))  # T
    # print("{} - {}".format(is_match("aac", "a*c"), is_match2("aac", "a*c")))  # T
    # print("{} - {}".format(is_match("aaaaaac", "a*c"), is_match2("aaaaaac", "a*c")))  # T
    # print("{} - {}".format(is_match("cc", "ccc"), is_match2("cc", "ccc")))  # F
    # print("{} - {}".format(is_match("abc", "a?b*"), is_match2("abc", "a?b*")))  # F
    # print("{} - {}".format(is_match("abbb", "a?b*"), is_match2("abbb", "a?b*")))  # T
    # print("{} - {}".format(is_match("abbb", "a?b*b"), is_match2("abbb", "a?b*b")))  # T
    # print("{} - {}".format(is_match("bbb", "a?b*bb"), is_match2("bbb", "a?b*bb")))  # F
    # print("{} - {}".format(is_match("aabbb", "a?b*b?b"), is_match2("aabbb", "a?b*b?b")))  # F
    # print("{} - {}".format(is_match("abbb", "a?b*bbb"), is_match2("abbb", "a?b*bbb")))  # F
    # print("{} - {}".format(is_match("adceb", "*a*b"), is_match2("adceb", "*a*b")))  # T
    # print("{} - {}".format(is_match("abcd", "*"), is_match2("abcd", "*")))  # T

    # print("{} - {}".format(is_match("abc", "abc"), "T"))  # T
    # print("{} - {}".format(is_match("abc", "a?c"), "T"))  # T
    # print("{} - {}".format(is_match("ac", "a?c"), "F"))  # F
    # print("{} - {}".format(is_match("aac", "a?c"), "T"))  # T
    # print("{} - {}".format(is_match("aac", "a*c"), "T"))  # T
    # print("{} - {}".format(is_match("aaaaaac", "a*c"), "T"))  # T
    # print("{} - {}".format(is_match("cc", "ccc"), "F"))  # F
    # print("{} - {}".format(is_match("abc", "a?b*"), "F"))  # F
    # print("{} - {}".format(is_match("abbb", "a?b*"), "T"))  # T
    # print("{} - {}".format(is_match("abbb", "a?b*b"), "T"))  # T
    # print("{} - {}".format(is_match("bbb", "a?b*bb"), "F"))  # F
    # print("{} - {}".format(is_match("aabbb", "a?b*b?b"), "F"))  # F
    # print("{} - {}".format(is_match("abbb", "a?b*bbb"), "F"))  # F
    # print("{} - {}".format(is_match("adceb", "*a*b"), "T"))  # T
    # print("{} - {}".format(is_match("abcd", "*"), "T"))  # T
