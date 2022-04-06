def kmp(s, t):
    pmt = [-1]
    i, j, LT, LS = 0, -1, len(t), len(s)
    while i < LT:
        if j == -1 or t[i] == t[j]:
            i += 1
            j += 1
            pmt.append(j)
        else:
            j = pmt[j]
    print(pmt)

    i, j = 0, 0
    while i < LS and j < LT:
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = pmt[j]

    if j == LT:
        return i - j
    else:
        return -1


if __name__ == '__main__':
    print(kmp("AABBCBBABBCACCD", "BBABBCAC"))
