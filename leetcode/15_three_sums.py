def three_sums(nums):
    L = len(nums)
    zero_sums = []
    for i in range(L-2):
        for j in range(i+1, L-1):
            for k in range(j+1, L):
                if nums[i] + nums[j] + nums[k] == 0:
                    if sorted([nums[i], nums[j], nums[k]]) not in zero_sums:
                        zero_sums.append(sorted([nums[i], nums[j], nums[k]]))
    return zero_sums


def three_sums2(nums):
    nums.sort()
    diff, L = 0, len(nums)
    zero_sums = []
    for i in range(L - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        low, high = i + 1, L - 1
        diff = -nums[i]
        while low < high:
            if nums[low] + nums[high] == diff:
                zero_sums.append([nums[low], nums[high], nums[i]])
                while low < high and nums[low] == nums[low+1]:
                    low += 1
                while low < high and nums[high] == nums[high-1]:
                    high -= 1
                low += 1
                high -= 1
            elif nums[low] + nums[high] < diff:
                low += 1
            else:
                high -= 1

    return zero_sums


if __name__ == '__main__':
    print(three_sums2([-1, 0, 1, 2, -1, -4]))
    print(three_sums2([1, 2, -2, -1]))
