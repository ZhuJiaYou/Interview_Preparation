def ugly_num(n):
    uglys = [1]
    pos_2 = 0
    pos_3 = 0
    pos_5 = 0
    for i in range(n - 1):
        ugly2, ugly3, ugly5 = uglys[pos_2]*2, uglys[pos_3]*3, uglys[pos_5]*5
        ugly_now = min(ugly2, ugly3, ugly5)
        uglys.append(ugly_now)
        if ugly2 == ugly_now:
            pos_2 += 1
        if ugly3 == ugly_now:
            pos_3 += 1
        if ugly5 == ugly_now:
            pos_5 += 1
    return uglys[-1]



if __name__ == '__main__':
    print(ugly_num(1))
    print(ugly_num(5))
    print(ugly_num(1500))
