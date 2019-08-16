from collections import deque


def count_inverse(data):
    count = 0
    
    def merge(left, right):
        nonlocal count
        q = deque()
        l, r = len(left) - 1, len(right) - 1
        while l >= 0 and r >= 0:
            if left[l] > right[r]:
                count += r + 1
                q.appendleft(left[l])
                l -= 1
            else:
                q.appendleft(right[r])
                r -= 1
        q = left[:l+1] + right[:r+1] + list(q)
        return q

    def merge_sort(ary):
        if len(ary) <= 1:
            return ary
        mid = len(ary) // 2
        left = merge_sort(ary[:mid])
        right = merge_sort(ary[mid:])
        return merge(left, right)
    merge_sort(data)
    return count


if __name__ == "__main__":
    print(count_inverse([7, 5, 6, 4]))
