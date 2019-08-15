from functools import reduce


def check(A):
    def helper_mul(x, y):
        if x == 0:
            x = 1
        if y == 0:
            y = 1
        return x * y

    if A.count(0) > 1:
        return [0] * len(A)
    total = reduce(helper_mul, A)
    has_0 = 0 in A
    ans = []
    for num in A:
        if num == 0:
            ans.append(total)
        elif has_0:
            ans.append(0)
        else:
            ans.append(total // num)
    return ans


def matrix_mul_without_division(A):
    C = [1]
    for i in range(1, len(A)):
        C.append(C[-1]*A[i-1])
    D = [1] * len(A)
    for i in range(len(A)-2, -1, -1):
        D[i] = D[i+1]*A[i+1]
    return [C[i]*D[i] for i in range(len(A))]


if __name__ == '__main__':
    print(matrix_mul_without_division(list(range(4, 10))) == check(list(range(4, 10))))





















