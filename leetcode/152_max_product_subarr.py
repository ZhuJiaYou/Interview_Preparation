def max_product_subarr(nums):
    maxs = [nums[0]]
    mins = [nums[0]]
    for n in nums[1:]:
        a = maxs[-1] * n
        b = mins[-1] * n
        maxs.append(max(a, b, n))
        mins.append(min(a, b, n))
    return(max(maxs))
        


if __name__ == '__main__':
    arr = [2, 3, -2, 4]
    # arr = [-2, 0, -1]
    print(max_product_subarr(arr))
