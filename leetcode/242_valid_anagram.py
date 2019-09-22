from collections import Counter


def is_anagram(s, t):
    return Counter(s) == Counter(t)


if __name__ == '__main__':
    print(is_anagram("anagram", "nagaram"))
    print(is_anagram("rat", "car"))
