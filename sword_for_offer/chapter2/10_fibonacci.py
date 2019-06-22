import functools


def fib(N: int) -> int:
    f0 = 0
    f1 = 1
    if N == 0:
        return f0
    elif N == 1:
        return f1
    else:
        for _ in range(2, N+1):
            f3 = f0 + f1
            f0, f1 = f1, f3
        return f3


@functools.lru_cache()
def fib2(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fib(N-1) + fib(N-2)


if __name__ == '__main__':
    print(fib(2))
    print(fib2(2))
