def sum_n(n):
    return n and n + sum_n(n-1)


if __name__ == '__main__':
    print(sum_n(10))
