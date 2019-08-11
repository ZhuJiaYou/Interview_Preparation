def find_continuous_sum(s):
    end = (s + 1) // 2
    first = 1
    last = 2
    now = 3
    results = []
    while last <= end:
        if now == s:
            results.append(list(range(first, last+1)))
            print(first, last, now)
            last += 1
            now += last
        elif now < s:
            last += 1
            now += last
        else:
            now -= first
            first += 1
    return results


if __name__ == '__main__':
    print(find_continuous_sum(100))
