def column_num(s):
    base = 1
    res = 0
    for c in s[::-1]:
        res += (ord(c)-ord('A')+1) * base
        base *= 26
    return res


if __name__ == '__main__':
    print(column_num("ZY"))
