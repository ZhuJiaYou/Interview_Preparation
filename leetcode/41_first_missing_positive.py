def first_missing_positive(nums):
    for i in range(len(nums)):
        if nums[i] != i + 1:
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


if __name__ == '__main__':
    a = [1, 2, 0]
    b = [3, 4, -1, 1]
    c = [7, 8, 9, 11, 12]
    print(first_missing_positive(a))
    print(first_missing_positive(b))
    print(first_missing_positive(c))
