import numpy as np


def sum_with_bit(a, b):
    while b != 0:
        a, b = np.int32(a^b), np.int32((a&b)<<1)
    return int(a)


def sum_with_bit2(a, b):
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a^b)&mask, ((a&b)<<1)&mask
    return a if a <= MAX else ~(a^mask)


if __name__ == '__main__':
    print(sum_with_bit(-11, 22))
    print(sum_with_bit(-11, 22))
