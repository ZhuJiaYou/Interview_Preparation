def merge_sorted(nums1, m, nums2, n):
    for _ in range(len(nums1)-m):
        nums1.pop()
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] >= nums2[j]:
            nums1.insert(i, nums2.pop(j))
            i += 1
        else:
            i += 1
    nums1 += nums2       


def merge_sorted2(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    nums1[:n] = nums2[:n]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    # merge_sorted(nums1, 3, nums2, 3)
    merge_sorted2(nums1, 3, nums2, 3)

    print(nums1)
