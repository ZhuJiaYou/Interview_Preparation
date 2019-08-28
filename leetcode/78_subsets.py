def subsets(nums):
    subsets = []
    def permutation(subset, i):
        if i == len(nums):
            subsets.append(subset[:])
            return
        permutation(subset, i+1)
        subset.append(nums[i])
        permutation(subset, i+1)
        subset.pop()
    permutation([], 0)
    return subsets


def subsets2(nums):
    subsets = [[]]
    for num in nums:
        subsets += [s + [num] for s in subsets]
    return subsets


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
    print(subsets2([1, 2, 3]))
