import functools


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    # @functools.lru_cache()
    def pow_with_unsigned(x, n):
        if n == 1:
            return x
        if n == 0:
            return 1

        res = pow_with_unsigned(x, n >> 1)
        res *= res
        if n & 1 == 1:
            res *= x
        return res

    if n < 0:
        return 1 / pow_with_unsigned(x, -n)
    else:
        return pow_with_unsigned(x, n)


if __name__ == '__main__':
    print(myPow(0.00001, 2147483647))
