def count_one(n):
    count = 0
    i = 1
    while i <= n:
        divider = i * 10
        count += n // divider * i  # (n % divider + 1) ~ n
        tmp = n % divider
        # 0 ~ n % divider
        if tmp < i:
            pass
        elif tmp >= 2 * i - 1:
            count += i
        else:
            count += tmp - i + 1
        # count += min(max(n % divider - i + 1, 0), i)
        i *= 10
    return count


if __name__ == '__main__':
    print(count_one(12))
