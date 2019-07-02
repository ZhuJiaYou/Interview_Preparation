def hamming_weight(n: int) -> int:  # Some Questions. MARK
    bits = 0
    while n:
        bits += 1
        n = n & (n - 1)
    return bits


if __name__ == '__main__':
#    print(hamming_weight(-11))
    print(bin(-11).count('1'))
