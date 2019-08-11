def find_sum(nums, s):
    low, high = 0, len(nums) - 1
    while low < high:
        if nums[low] + nums[high] == s:
            return nums[low], nums[high]
        elif nums[low] + nums[high] < s:
            low += 1
        else:
            high -= 1
    return None


if __name__ == '__main__':
    nums = [1, 2, 4, 7, 11, 15]
    print(find_sum(nums, 15))
