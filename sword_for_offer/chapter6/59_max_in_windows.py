from collections import deque


def max_in_windows(nums, n):
    if n < 1:
        return []
    results = []
    q = deque()
    for i in range(len(nums)):
        if q and i - q[0] >= n:
            # print(q)
            # print("********************************************************************************")
            q.popleft()
        print(q)
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        q.append(i)
        if i >= n - 1:
            results.append(nums[q[0]])
        # print(q)
    return results


if __name__ == '__main__':
    nums = [2, 3, 4, 2, 6, 2, 5, 1]
    print(max_in_windows(nums, 3))
