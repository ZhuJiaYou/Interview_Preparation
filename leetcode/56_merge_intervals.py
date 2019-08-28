def merge_intervals(intervals):
    intervals.sort()
    i = 0
    while i < len(intervals)-1:
        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
            intervals.pop(i+1)
        else:
            i += 1
    return intervals


if __name__ == '__main__':
    intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
    print(merge_intervals(intervals))
