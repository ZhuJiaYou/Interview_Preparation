def partition(s):
    def is_palindrome(ss):
        low, high = 0, len(ss)-1
        while low < high:
            if ss[low] != ss[high]:
                return False
            else:
                low += 1
                high -= 1
        return True

    partitions = []
    def dfs(pt, sss):
        nonlocal partitions
        if not sss:
            partitions.append(pt[:])
        for i in range(1, len(sss)+1):
            if is_palindrome(sss[:i]):
                pt.append(sss[:i])
                dfs(pt, sss[i:])
                pt.pop()

    dfs([], s)
    return partitions





if __name__ == '__main__':
    s = "aab"
    print(partition(s))
    s = "abc"
    print(partition(s))
