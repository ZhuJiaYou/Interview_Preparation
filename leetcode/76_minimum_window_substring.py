from collections import Counter


def min_window(s, t):
    need = Counter(t)
    missing = len(t)

    start, end = 0, 0  # window start and end
    i = 0  # i, j are start and end of search
    for j, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:  # match all chars
            while need[s[i]] < 0:  # remove chars to find the real start
                need[s[i]] += 1
                i += 1
            need[s[i]] += 1  # make sure the first appearing char satisfies need[char]>0
            missing += 1  # we missed this first char, so add missing by 1
            if end == 0 or j-i < end-start:  # update window
                start, end = i, j
            i += 1  # update i to start+1 for next window
    return s[start:end]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(min_window(s, t))
