def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) < 3:
        return max(nums)

    maxs = []
    maxs.append(nums[0])
    maxs.append(nums[1])
    maxs.append(nums[0] + nums[2])
    for i in range(3, len(nums)):
        maxs.append(max(maxs[i-2], maxs[i-3]) + nums[i])
    # print(maxs)
    return max(maxs[-1], maxs[-2])


if __name__ == '__main__':
    nums = [2, 1, 1, 2]
    print(rob(nums))
