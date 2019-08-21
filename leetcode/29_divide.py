def divide(dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    res = 0
    while dividend >= divisor:
        i, t_divisor = 1, divisor
        while dividend >= t_divisor:
            dividend -= t_divisor
            res += i
            i <<= 1
            t_divisor <<= 1
    if not positive:
        res = -res
    return min(max(res, -2147483648), 2147483647)


if __name__ == '__main__':
    print(divide(100, 3))
