def last_left_in_circle(n, m):
    left = 0
    for i in range(1, n):
        left = (left + m) % (i+1)
    return left


if __name__ == '__main__':
    print(last_left_in_circle(5, 3))
