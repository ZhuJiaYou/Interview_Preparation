def left_rotate_string(s, n):
    return s[2:] + s[:2]

if __name__ == '__main__':
    s = 'abcde'
    print(left_rotate_string(s, 2))
