def find_nth_digit(n):
    start, step, size = 1, 9, 1
    while n > size * step:
        n, start, step, size = n-size*step, start*10, step*10, size+1
    return int(str(start + (n-1)//size)[(n-1) % size])   


if __name__ == '__main__':
    print(find_nth_digit(11))
