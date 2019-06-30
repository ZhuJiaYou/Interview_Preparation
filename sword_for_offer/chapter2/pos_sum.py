def pos_sum(a):
    s = 0
    while a != 0:
        s += (a % 10)
        a = a // 10
    return s


def pos_sum2(a):
    return sum(map(int, str(a)))


if __name__ == "__main__":
    print(pos_sum2(123))
