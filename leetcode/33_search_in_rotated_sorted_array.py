def search(nums, target):
    if nums == []:
        return -1

    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] > nums[low]:
            low = mid
        elif nums[mid] < nums[high]:
            high = mid
        else:
            min_index = high
            break

    if min_index == 0:
        lowleft, highleft = -1, -1
    else:
        lowleft, highleft = 0, min_index-1
    lowright, highright = min_index, len(nums)-1

    
    print(lowleft, highleft, lowright, highright)

    if nums[lowright] <= target <= nums[highright]:
        low, high = lowleft, highleft
    elif nums[lowleft] <= target <= nums[highleft]:
        low, high = lowright, highright
    else:
        return -1

    while low < high:
        print(low, high)
        mid = (low+high)//2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] < target):
            low = mid + 1
        else:
            high = mid - 1

    if nums[low] == target:
        return (low+len(nums))%len(nums)
    else:
        return -1


if __name__ == '__main__':
    nums = [1]
    print(search(nums, 1))
