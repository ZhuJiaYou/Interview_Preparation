def nums2str_ways(s):
    ways = int(s > '')
    pre_ways = 0
    pre = ''
    for d in s:
        pre_ways, ways, pre = ways, ways + (9<int(pre+d)<27) * pre_ways, d
    return ways


if __name__ == '__main__':
    print(nums2str_ways('12258'))
