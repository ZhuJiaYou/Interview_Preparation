def climb_stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    f1, f2 = 1, 2
    fn = 0
    for _ in range(n-2):
        fn = f1 + f2
        f1, f2 = f2, fn
    return fn


if __name__ == '__main__':
    print(climb_stairs(4))
