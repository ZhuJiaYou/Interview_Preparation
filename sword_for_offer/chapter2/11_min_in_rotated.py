def find_min(nums: 'list[int]') -> int:
    left = 0
    right = len(nums) - 1
    if nums[left] < nums[right]:  # Notice
        return nums[left]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[left]:
            left = mid
        else:
            return nums[right]  # Notice "R"


if __name__ == '__main__':
    print(find_min([3, 4, 5, 1, 2]))
    print(find_min([4, 5, 0, 1, 2, 3]))
    print(find_min([0, 1, 2, 3, 4]))
