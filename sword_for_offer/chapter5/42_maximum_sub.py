def max_sum_array(a):
    max_i = a[:]
    for i in range(len(a)):
        if i > 0 and max_i[i-1] > 0:
            max_i[i] += max_i[i-1]
    return max(max_i)


if __name__ == '__main__':
    a = [1, -2, 3, 10, -4, 7, 2, -5]
    print(max_sum_array(a))
