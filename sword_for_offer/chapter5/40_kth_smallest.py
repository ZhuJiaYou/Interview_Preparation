from random import randint
import heapq


def get_small_numbers(a, k):
    def partition(s, e):
        low = s
        high = e
        p = randint(s, e)  # eliminate denpendence on the first num
        nums[s], nums[p] = nums[p], nums[s]
        p = nums[s]
        while low < high:
            while high > low and a[high] >= p:
                high -= 1
            a[low] = a[high]
            while high > low and a[low] <= p:
                low += 1
            a[high] = a[low]
        a[low] = p
        return low

    start = 0
    end = len(a) - 1
    pivot = partition(start, end)
    while pivot != k - 1:
        if pivot >= k:
            end = pivot - 1
        else:
            start = pivot + 1
        pivot = partition(start, end)
    return a[:pivot+1]


def get_small_numbers2(a, k):
    # heapq.heapify(a)
    return heapq.nsmallest(k, a)


if __name__ == '__main__':
    nums = [4, 5, 1, 2, 6, 7, 3, 8]
    print(get_small_numbers(nums, 4))
    print(get_small_numbers2(nums, 4))
