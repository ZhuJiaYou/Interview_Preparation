def reverse_bin(n):
    n = '{0:032b}'.format(n)
    n = n[::-1]
    return int(n, 2)
    # n = n[:2] + n[2:][::-1]
    # print(hex(n))




if __name__ == '__main__':
    print(reverse_bin(5))
