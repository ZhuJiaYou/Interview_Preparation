def search_range(nums, target):
    left, right = -1, -1
    l_ = len(nums)
    low = 0
    high = l_ - 1
    while low < high:
        print(low, high)
        print("&&&&&&&&&&&&&&&&&&&&")
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        elif (mid-1 >= 0) and (nums[mid-1] == target):
            high = mid - 1
        elif (mid == 0) or ((mid-1 >= 0) and (nums[mid-1] != target)):
            left = mid
            break;
    if nums[low] == target and left == -1:
        left = low
    low = 0
    high = l_ - 1
    while low < high:
        print(low, high)
        print("***************")
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        elif (mid+1 < l_) and (nums[mid+1] == target):
            low = mid + 1
        elif (mid == l_-1) or ((mid+1 < l_) and (nums[mid+1] != target)):
            right = mid
            break;
    if nums[low] == target and right == -1:
        right = low
    return left, right


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 2
    print(search_range(nums, target))
