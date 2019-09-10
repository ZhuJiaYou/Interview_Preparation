def rotate_array(nums, k):
    k = k % len(nums)
    def rotate(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    rotate(0, len(nums)-1)
    rotate(0, k-1)
    rotate(k, len(nums)-1)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    rotate_array(nums, 3)
    print(nums)
