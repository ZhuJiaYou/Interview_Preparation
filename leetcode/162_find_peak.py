def find_peak(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right) // 2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        if nums[mid] < nums[mid]+1:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(find_peak(nums))
