def get_num_same_as_index(nums):
    if nums[0] > 0:
        return -1
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == mid:
            return mid
        elif nums[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    return low


if __name__ == "__main__":
    print(get_num_same_as_index([-3, -1, 1, 3, 5]))
    print(get_num_same_as_index([1, 2, 3]))
    print(get_num_same_as_index([0]))

