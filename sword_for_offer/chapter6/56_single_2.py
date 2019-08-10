def single2num(nums):
    judge = nums[0]
    for num in nums[1:]:
        judge ^= num

    mask = 1
    while judge & mask == 0:
        mask <<= 1

    low, high = 0, len(nums) - 1
    while low < high:
        while low < high and nums[low] & mask != 0:
            low += 1
        while low < high and nums[high] & mask == 0:
            high -= 1
        nums[low], nums[high] = nums[high], nums[low]

    if nums[low] & mask == 0:
        second = low
    else:
        second = low + 1

    a = nums[0]
    for num in nums[1:second]:
        a ^= num
    b = nums[second]
    for num in nums[second+1:]:
        b ^= num

    return a, b


if __name__ == '__main__':
    nums = [2, 4, 3, 6, 3, 2, 5, 5]
    print(single2num(nums))
