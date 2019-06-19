def duplicate(numbers: list) -> int:
    for i, num in enumerate(numbers):
        while num != i:
            if numbers[num] == num:
                return True, num
            else:
                numbers[i], numbers[num] = numbers[num], numbers[i]
                num = numbers[i]
    return False, None


def duplicate_no_change(nums: list) -> int:
    """
    You cannot change the origin list
    Time complexity: O(nlog(n))
    Spatial complexity: O(1)
    """
    low = 1
    high = len(nums) - 1
    while(high >= low):
        mid = (high + low) // 2
        n = sum(low <= i <= mid for i in nums)
        if high == low:
            if n > 1:
                return high
            else:
                break
        else:
            if n > mid - low + 1:
                high = mid  # NOTICE
            else:
                low = mid + 1
    return -1


def duplicate_no_change2(nums: list) -> int:
    """
    You cannot change the origin list
    Time complexity: O(nlog(n))
    Spatial complexity: O(1)
    """
    numbers = nums[:]
    for i, num in enumerate(numbers):
        while num != i:
            if numbers[num] == num:
                return num
            else:
                numbers[i], numbers[num] = numbers[num], numbers[i]
                num = numbers[i]
    return -1


if __name__ == '__main__':
    print(duplicate_no_change2([2, 5, 4, 3, 3, 6, 1, 7]))
