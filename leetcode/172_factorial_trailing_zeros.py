def fact_trail_zero(n):
    res = 0
    while n:
        n //= 5
        res += n
    return res


if __name__ == '__main__':
    n = 10
    print(fact_trail_zero(n))
