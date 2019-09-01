def longest_consecutive_seq(nums):
    nums = set(nums)
    longest = 0
    now, now_conse = 0, 0
    for num in nums:
        if num-1 not in nums:
            now, now_conse = num, 1
            while now+1 in nums:
                now += 1
                now_conse += 1
            longest = max(longest, now_conse)
    return longest    


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive_seq(nums))
