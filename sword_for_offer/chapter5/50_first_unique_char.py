from collections import Counter


def first_unique_char(s):
    c = Counter(s)
    for i, ch in enumerate(s):
        if c[ch] == 1:
            return ch
    return ''


if __name__ == '__main__':
    s = 'google'
    print(first_unique_char(s))
