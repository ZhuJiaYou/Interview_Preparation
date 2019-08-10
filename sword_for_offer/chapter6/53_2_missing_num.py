def find_missing(nums):
    if nums == []:
        return 0
    elif nums[-1] == len(nums) - 1:
        return len(nums)
    low = 0
    high = len(nums) - 1
    while low < high:
        print(low, high)
        print("&&&&&&&&&&&&&&&&&&&&")
        mid = (low + high) // 2
        print(mid, nums[mid-1])
        if nums[mid] == mid:
            low = mid + 1
        elif (mid-1 >= 0) and (nums[mid-1] == mid-1):
            return mid
        elif (mid == 0) or ((mid-1 >= 0) and (nums[mid-1] == mid)):
            high = mid - 1
    return low


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 6, 7, 8, 9]
    print(find_missing(nums))
