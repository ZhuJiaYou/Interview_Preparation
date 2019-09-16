def find_median_sorted_arrs(nums1, nums2):
    def kth(A, B, k):
        if not A:
            return B[k]
        if not B:
            return A[k]
        ia, ib = len(A)//2, len(B)//2
        a, b = A[ia], B[ib]
        if ia+ib < k:
            if a > b:
                return kth(A, B[ib+1:], k-ib-1)
            else:
                return kth(A[ia+1:], B, k-ia-1)
        else:
            if a > b:
                return kth(A[:ia], B, k)
            else:
                return kth(A, B[:ib], k)

    L = len(nums1) + len(nums2)
    if L % 2 == 1:
        return kth(nums1, nums2, L//2)
    else:
        return (kth(nums1, nums2, L//2) + kth(nums1, nums2, L//2-1))/2


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(find_median_sorted_arrs(nums1, nums2))
