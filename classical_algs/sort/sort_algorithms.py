# stable
# time avg: O(n2), time worst: O(n2), time best: O(n)
# space: O(1)
def bubble_sort(arr):
    for i in range(1, len(arr)):  # NOTICE THE <1>
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# unstable
# time avg: O(n2), time worst: O(n2), time best: O(n2)
# space: O(1)
def selection_sort(arr):
    for i in range(len(arr)-1):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[mini] > arr[j]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]


# stable
# time avg: O(n2), time worst: O(n2), time best: O(n)
# space: O(1)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# unstable
# time avg: O(nlogn2), time worst: O(nlogn2), time best: O(nlogn)
# space: O(1)
def shell_sort(arr):
    k = len(arr) // 2
    while k > 0:
        for m in range(k):
            for n in range(m+k, len(arr), k):
                for p in range(n-k, -1, -k):
                    if arr[p] > arr[p+k]:
                        arr[p], arr[p+k] = arr[p+k], arr[p]
        k = k // 2


# stable
# time avg: O(nlogn), time worst: O(nlogn), time best: O(nlogn)
# space: O(n)
def merge_sort(arr):
    def merge(left, right):
        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        return merged + left + right

    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge_sort2(arr):
    def merge(left, right):
        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        return merged + left + right

    if len(arr) < 2:
        return
    merged = arr
    n = len(arr)
    size = 1
    while size < n:
        for i in range(0, n-size, size+size):
            merged[i:min(n, i+size+size)] = merge(merged[i:i+size], merged[i+size:min(n, i+size+size)])
        size += size
    # arr = merged


# unstable
# time avg: O(nlogn), time worst: O(n2), time best: O(nlogn)
# space: O(logn)
def quick_sort(arr, low=None, high=None):
    def partition(a, low, high):
        pivot_val = a[low]
        while low < high:
            while low < high and a[high] >= pivot_val:
                high -= 1
            a[low] = a[high]
            while low < high and a[low] <= pivot_val:
                low += 1
            a[high] = a[low]
        a[low] = pivot_val
        return low

    l_ = 0 if low is None else low
    h = len(arr) - 1 if high is None else high 
    if l_ < h:
        pivot_pos = partition(arr, l_, h)
        quick_sort(arr, l_, pivot_pos-1)
        quick_sort(arr, pivot_pos+1, h)


# unstable
# time avg: O(nlogn), time worst: O(nlogn), time best: O(nlogn)
# space: O(1)
def heap_sort(arr):
    def siftdown(a, adjust, begin, end):
        i, j = begin, begin * 2 + 1  # j is the LeftNode of i, NOTICE the start index is 0
        while j < end:
            if j + 1 < end and a[j+1] > a[j]:
                j += 1
            if adjust > a[j]:
                break
            a[i] = a[j]
            i, j = j, j * 2 + 1
        a[i] = adjust

    end = len(arr)
    for i in range(end//2-1, -1, -1):
        siftdown(arr, a[i], i, end)
    for i in range(end-1, 0, -1):
        # print(arr)
        adjust = arr[i]
        arr[i] = arr[0]
        siftdown(a, adjust, 0, i)


# stable
# time avg: O(n+k), time worst: O(n+k), time best: O(n+k), k is the range of input data
# space: O(k)
# input data must be integers with a definite range
def counting_sort(arr, max_val):
    bucket = [0] * (max_val + 1)
    for i in arr:
        bucket[i] += 1
    sorted_i = 0
    for i in range(len(bucket)):
        while bucket[i] > 0:
            arr[sorted_i] = i
            sorted_i += 1
            bucket[i] -= 1




if __name__ == '__main__':
    a = [2, 8, 5, 7, 2, 3, 0, 4]
    # bubble_sort(a)
    # selection_sort(a)
    # insertion_sort(a)
    # print(merge_sort(a))
    # merge_sort2(a)
    # quick_sort(a)
    # heap_sort(a)
    counting_sort(a, 9)
    print(a)
