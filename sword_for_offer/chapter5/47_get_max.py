def get_max(m):
    R, C = len(m), len(m[0])
    pre_line_max = [0] * C
    for i in range(R):
        for j in range(C):
            if j > 0:
                pre_line_max[j] = max(pre_line_max[j], pre_line_max[j-1]) + m[i][j]
            else:
                pre_line_max[j] = pre_line_max[j] + m[i][j]
    return pre_line_max[-1]



if __name__ == '__main__':
    m = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(get_max(m))
