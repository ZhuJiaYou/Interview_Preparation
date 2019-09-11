def is_happy(n):
    def cal_next(x):
        next = 0
        while x:
            next += (x % 10) ** 2
            x //= 10
        return next

    his = []
    while n not in his:
        # print(cal_next(n))
        if n == 1:
            return True
        his.append(n)
        n = cal_next(n)
    return False





if __name__ == '__main__':
    n = 19
    print(is_happy(n))
