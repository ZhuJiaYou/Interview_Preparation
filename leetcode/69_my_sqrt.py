def my_sqrt(x):
    if x == 1 or x == 2 or x == 3:
        return 1
    elif x == 4:
        return 2
    elif x == 0:
        return 0
    for i in range(2, x//2+1):
        if i*i <= x and (i+1)*(i+1) > x:
            return i    


def my_sqrt2(x):
    low, high = 0, x
    while low < high:
        mid = (low + high) // 2
        if mid*mid <= x < (mid+1)*(mid+1):
            return mid
        elif mid*mid > x:
            high = mid
        else:
            low = mid + 1
    return low













if __name__ == '__main__':
    x = 50
    print(my_sqrt2(x))
