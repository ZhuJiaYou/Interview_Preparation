def reverse_words(s):
    return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    s = "the sky is blue"
    print(reverse_words(s))
