def count_primes(n):
    if n < 2:
        return 0
    primes = [True] * (n)
    primes[0], primes[1] = False, False
    for i in range(2, n):
        if primes[i]:
            for j in range(i*2, n, i):
                primes[j] = False
    # print(primes)
    return sum(primes)


if __name__ == '__main__':
    print(count_primes(10))
